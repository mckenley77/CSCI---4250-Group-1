# tests/test_messages.py

def create_student(client, username, first, last, major="Nursing"):
    payload = {
        "user_type": "student",
        "username": username,
        "password": "pw",
        "firstname": first,
        "lastname": last,
        "studentid": 0,
        "major": major,
        "locationsharingenabled": True,
    }
    resp = client.post("/students/", json=payload)
    assert resp.status_code == 200


def test_create_message_and_get_by_user(client):
    # Create two students: sender (id=0), recipient (id=1)
    create_student(client, "sender", "Sender", "User")
    create_student(client, "recipient", "Recipient", "User")

    # Create a message
    message_payload = {
        "messageid": 0,
        "senderId": 0,
        "sendername": "Sender User",
        "recipientid": 1,
        "recipientname": "Recipient User",
        "recipienttype": "student",
        "messagecontent": "Hello there",
        "isread": False,
    }

    resp = client.post("/messages/", json=message_payload)
    assert resp.status_code == 200
    assert resp.json() == "success"

    # All messages
    resp = client.get("/messages/")
    assert resp.status_code == 200
    messages = resp.json()
    assert len(messages) == 1

    msg = messages[0]
    assert msg["senderId"] == 0
    assert msg["recipientid"] == 1
    assert msg["messagecontent"] == "Hello there"

    # Messages for sender
    resp = client.get("/messages/0")
    assert resp.status_code == 200
    msgs_for_sender = resp.json()
    assert len(msgs_for_sender) == 1

    # Messages for recipient
    resp = client.get("/messages/1")
    assert resp.status_code == 200
    msgs_for_recipient = resp.json()
    assert len(msgs_for_recipient) == 1


def test_delete_message(client):
    create_student(client, "sender", "Sender", "User")
    create_student(client, "recipient", "Recipient", "User")

    message_payload = {
        "messageid": 0,
        "senderId": 0,
        "sendername": "Sender User",
        "recipientid": 1,
        "recipientname": "Recipient User",
        "recipienttype": "student",
        "messagecontent": "To be deleted",
        "isread": False,
    }

    resp = client.post("/messages/", json=message_payload)
    assert resp.status_code == 200

    # There should now be one message
    resp = client.get("/messages/")
    assert resp.status_code == 200
    messages = resp.json()
    assert len(messages) == 1

    msg_id = messages[0]["id"]

    # Delete it
    resp = client.delete(f"/messages/{msg_id}")
    assert resp.status_code == 200
    assert "successfully deleted message" in resp.json()

    # Confirm empty
    resp = client.get("/messages/")
    assert resp.status_code == 200
    assert resp.json() == []
