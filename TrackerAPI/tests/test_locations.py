# tests/test_locations.py
from datetime import datetime

def test_create_and_list_locations(client):
    payload = {
        "id": 0,
        "userid": 42,
        "latitude": 36.1234,
        "longitude": -82.3456,
        "address": "Test Street 1",
        "timestamp": datetime.utcnow().isoformat(),
        "accuracy": 5.0,
    }

    resp = client.post("/location/", json=payload)
    assert resp.status_code == 200
    assert resp.json() == "success"

    resp = client.get("/location/")
    assert resp.status_code == 200
    locations = resp.json()
    assert len(locations) == 1

    loc = locations[0]
    assert loc["userid"] == 42
    assert loc["address"] == "Test Street 1"
    assert loc["latitude"] == 36.1234
    assert loc["longitude"] == -82.3456
