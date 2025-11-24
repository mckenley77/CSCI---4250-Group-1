# tests/test_users.py

def test_create_user_and_list_users(client):
    # Create a user
    payload = {
        "user_type": "student",
        "username": "testuser",
        "password": "secret123",
        "firstname": "Test",
        "lastname": "User",
    }

    resp = client.post("/users/", json=payload)
    assert resp.status_code == 200
    assert resp.json() == "success"

    # List users
    resp = client.get("/users/")
    assert resp.status_code == 200

    users = resp.json()
    assert isinstance(users, list)
    assert len(users) == 1

    u = users[0]
    assert u["username"] == "testuser"
    assert u["firstname"] == "Test"
    assert u["lastname"] == "User"
    assert u["user_type"] == "student"


def test_get_user_by_id_and_delete(client):
    # First create a user
    payload = {
        "user_type": "instructor",
        "username": "prof",
        "password": "pw",
        "firstname": "Prof",
        "lastname": "X",
    }
    resp = client.post("/users/", json=payload)
    assert resp.status_code == 200

    # With fresh test DB, first user should have id = 0
    user_id = 0

    # Get by id
    resp = client.get(f"/users/{user_id}")
    assert resp.status_code == 200

    user = resp.json()
    assert user["id"] == user_id
    assert user["username"] == "prof"

    # Delete
    resp = client.delete(f"/users/{user_id}")
    assert resp.status_code == 200
    assert "successfully deleted user" in resp.json()

    # Confirm gone
    resp = client.get("/users/")
    assert resp.status_code == 200
    assert resp.json() == []
