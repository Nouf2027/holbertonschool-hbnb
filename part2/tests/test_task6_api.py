import uuid
import pytest

BASE = "/api/v1"

def _u():
    return str(uuid.uuid4())[:8]

def test_swagger_available(client):
    res = client.get(f"{BASE}/")
    assert res.status_code == 200

def test_create_place_invalid_missing_name(client):
    res = client.post(f"{BASE}/places/", json={
        "description": "Test",
        "price_per_night": 100,
        "latitude": 0,
        "longitude": 0,
        "owner_id": "invalid"
    })
    assert res.status_code == 400

def test_get_place_not_found(client):
    res = client.get(f"{BASE}/places/does-not-exist")
    assert res.status_code == 404

def test_create_review_invalid_missing_text(client):
    
    res = client.post(f"{BASE}/reviews/", json={
        "rating": 5,
        "user_id": "invalid",
        "place_id": "invalid"
    })
    assert res.status_code == 400

def test_get_review_not_found(client):
    res = client.get(f"{BASE}/reviews/does-not-exist")
    assert res.status_code == 404
