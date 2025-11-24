# tests/test_students.py

def test_create_and_get_students(client):
    payload = {
        "user_type": "student",
        "username": "stud1",
        "password": "pw1",
        "firstname": "Student",
        "lastname": "One",
        "studentid": 123,
        "major": "Nursing",
        "locationsharingenabled": True,
    }

    resp = client.post("/students/", json=payload)
    assert resp.status_code == 200
    assert resp.json() == "success"

    # List students
    resp = client.get("/students/")
    assert resp.status_code == 200
    students = resp.json()
    assert isinstance(students, list)
    assert len(students) == 1

    s = students[0]
    assert s["username"] == "stud1"
    assert s["firstname"] == "Student"
    assert s["lastname"] == "One"
    assert s["major"] == "Nursing"
    assert s["locationsharingenabled"] is True


def test_delete_student(client):
    payload = {
        "user_type": "student",
        "username": "stud2",
        "password": "pw2",
        "firstname": "Student",
        "lastname": "Two",
        "studentid": 456,
        "major": "CS",
        "locationsharingenabled": True,
    }
    resp = client.post("/students/", json=payload)
    assert resp.status_code == 200

    # In a fresh DB, this student's shared user id should be 0
    student_id = 0

    resp = client.delete(f"/students/{student_id}")
    assert resp.status_code == 200
    assert "successfully deleted student" in resp.json()

    resp = client.get("/students/")
    assert resp.status_code == 200
    assert resp.json() == []
