import os
import json
import unittest
from urllib import request as ureq
from urllib.error import HTTPError, URLError

BASE = os.environ.get("BASE", "http://127.0.0.1:5000").rstrip("/")

def http(method, path, payload=None, headers=None, timeout=5):
    url = f"{BASE}{path}"
    data = None
    hdrs = {"Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        hdrs["Content-Type"] = "application/json"
    req = ureq.Request(url, data=data, headers=hdrs, method=method)
    try:
        with ureq.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return resp.status, body
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return e.code, body
    except URLError as e:
        raise RuntimeError(f"Cannot reach server at {BASE}: {e}")

def json_load(body):
    try:
        return json.loads(body)
    except Exception:
        return None

def extract_id(body):
    obj = json_load(body)
    if isinstance(obj, dict) and "id" in obj:
        return obj["id"]
    return None

class TestEndpointsBlackBox(unittest.TestCase):
    def test_swagger_available(self):
        code, _ = http("GET", "/api/v1/")
        self.assertIn(code, (200, 302, 308))

    def test_places_create_invalid_missing_title(self):
        code, _ = http("POST", "/api/v1/places/", {
            "description": "No title",
            "price": 100,
            "latitude": 24.7,
            "longitude": 46.6,
            "owner_id": "fake-owner-id"
        })
        self.assertEqual(code, 400)

    def test_places_get_not_found(self):
        code, _ = http("GET", "/api/v1/places/does-not-exist")
        self.assertEqual(code, 404)

    def test_reviews_create_invalid_missing_text(self):
        code, _ = http("POST", "/api/v1/reviews/", {
            "rating": 5,
            "user_id": "fake-user",
            "place_id": "fake-place"
        })
        self.assertEqual(code, 400)

    def test_reviews_get_not_found(self):
        code, body = http("GET", "/api/v1/reviews/does-not-exist")
        self.assertEqual(code, 404, msg=f"Expected 404, got {code}. Body:\n{body}")

    def test_place_reviews_place_not_found(self):
        code, _ = http("GET", "/api/v1/places/does-not-exist/reviews")
        self.assertEqual(code, 404)

    def test_optional_review_success_flow_if_possible(self):
        users_code, users_body = http("GET", "/api/v1/users/")
        if users_code == 404:
            self.skipTest("Users endpoint not available; skipping success flow.")

        users_obj = json_load(users_body)
        user_id = None
        if isinstance(users_obj, list) and len(users_obj) > 0 and isinstance(users_obj[0], dict):
            user_id = users_obj[0].get("id")

        if not user_id:
            create_code, create_body = http("POST", "/api/v1/users/", {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com"
            })
            if create_code not in (200, 201):
                self.skipTest(f"User creation rejected by API (status={create_code}); skipping success flow.")
            user_id = extract_id(create_body)

        if not user_id:
            self.skipTest("Could not obtain a valid user_id; skipping success flow.")

        place_code, place_body = http("POST", "/api/v1/places/", {
            "title": "Place For Review",
            "description": "D",
            "price": 120,
            "latitude": 24.7,
            "longitude": 46.6,
            "owner_id": user_id
        })
        if place_code not in (200, 201):
            self.skipTest(f"Place creation failed (status={place_code}); skipping success flow.")
        place_id = extract_id(place_body)

        if not place_id:
            self.skipTest("Could not extract place_id; skipping success flow.")

        review_code, review_body = http("POST", "/api/v1/reviews/", {
            "text": "Great place",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        self.assertEqual(review_code, 201, msg=f"Expected 201, got {review_code}. Body:\n{review_body}")
        review_id = extract_id(review_body)
        self.assertTrue(review_id)

        code, _ = http("GET", f"/api/v1/reviews/{review_id}")
        self.assertEqual(code, 200)

        code, _ = http("PUT", f"/api/v1/reviews/{review_id}", {"text": "Updated", "rating": 4})
        self.assertEqual(code, 200)

        code, _ = http("DELETE", f"/api/v1/reviews/{review_id}")
        self.assertEqual(code, 200)

if __name__ == "__main__":
    unittest.main(verbosity=2)
