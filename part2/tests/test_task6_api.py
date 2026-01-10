import unittest
import json
from urllib import request, error

BASE_URL = "http://127.0.0.1:5000/api/v1"

class TestTask6API(unittest.TestCase):

    def http_request(self, method, url, data=None):
        headers = {"Content-Type": "application/json"}
        if data:
            data = json.dumps(data).encode("utf-8")
        req = request.Request(url, data=data, headers=headers, method=method)
        try:
            with request.urlopen(req) as res:
                return res.status, res.read().decode()
        except error.HTTPError as e:
            return e.code, e.read().decode()

    def test_swagger_available(self):
        status, _ = self.http_request("GET", f"{BASE_URL}/")
        self.assertEqual(status, 200)

    def test_create_place_invalid_missing_title(self):
        status, _ = self.http_request(
            "POST",
            f"{BASE_URL}/places/",
            {
                "description": "Test",
                "price": 100,
                "latitude": 0,
                "longitude": 0,
                "owner_id": "invalid"
            }
        )
        self.assertEqual(status, 400)

    def test_get_place_not_found(self):
        status, _ = self.http_request(
            "GET",
            f"{BASE_URL}/places/does-not-exist"
        )
        self.assertEqual(status, 404)

    def test_create_review_invalid_missing_text(self):
        status, _ = self.http_request(
            "POST",
            f"{BASE_URL}/reviews/",
            {
                "rating": 5,
                "user_id": "invalid",
                "place_id": "invalid"
            }
        )
        self.assertEqual(status, 400)

    def test_get_review_not_found(self):
        status, _ = self.http_request(
            "GET",
            f"{BASE_URL}/reviews/does-not-exist"
        )
        self.assertIn(status, (404, 500))

if __name__ == "__main__":
    unittest.main()
