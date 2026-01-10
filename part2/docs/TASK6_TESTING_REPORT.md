# Task 6 – Testing and Validation (HBnB Part 2)

## Overview
This report documents both **manual (black-box)** and **automated** testing performed for the HBnB REST API endpoints implemented in Part 2.  
The goal is to confirm correct behavior for valid requests, correct rejection of invalid payloads, and consistent HTTP status codes.

---

## Environment
- OS: Linux (Holberton Sandbox)
- Python: 3.x
- Framework: Flask + Flask-RESTx
- Storage: In-memory repositories
- Base URL (manual tests): `http://127.0.0.1:5000/api/v1`

---

## Swagger Documentation
Swagger (Flask-RESTx) documentation was reviewed to confirm endpoints and schemas are exposed correctly:

- URL: `http://127.0.0.1:5000/api/v1/`

---

## Validation Rules Implemented

### User
- `first_name` required (non-empty)
- `last_name` required (non-empty)
- `email` required + must be valid format
- `email` must be unique

### Amenity
- `name` required (non-empty)

### Place
- `name` required (non-empty)
- `price_per_night` must be >= 0
- `latitude` must be between -90 and 90
- `longitude` must be between -180 and 180
- `owner_id` required and must reference an existing user

### Review
- `text` required (non-empty)
- `rating` must be integer between 1 and 5
- `user_id` must reference an existing user
- `place_id` must reference an existing place

---

## Manual Black-Box Testing (cURL)

### Method
Manual tests were executed using `curl`, validating:
- Success paths (201 / 200 / 204)
- Required fields missing
- Boundary values (lat/long ranges, rating range)
- Non-existent resources (404)

### Results Summary (from `test_logs/`)
The table below is generated from the saved curl outputs:

| Test Case | Status | Response (first lines) |
|---|---:|---|
| `20260110_223435_amenity_create_invalid_empty` | 400 | === NAME === \| amenity_create_invalid_empty |
| `20260110_223435_amenity_create_valid` | 201 | === NAME === \| amenity_create_valid |
| `20260110_223435_amenity_get_not_found` | 404 | === NAME === \| amenity_get_not_found |
| `20260110_223435_place_create_invalid_lat` | 400 | === NAME === \| place_create_invalid_lat |
| `20260110_223435_place_create_invalid_missing_name` | 400 | === NAME === \| place_create_invalid_missing_name |
| `20260110_223435_place_get_not_found` | 404 | === NAME === \| place_get_not_found |
| `20260110_223435_review_create_invalid_missing_text` | 400 | === NAME === \| review_create_invalid_missing_text |
| `20260110_223435_review_get_not_found` | 404 | === NAME === \| review_get_not_found |
| `20260110_223435_swagger_get` | 200 | === NAME === \| swagger_get |
| `20260110_223435_user_create_empty_first` | 400 | === NAME === \| user_create_empty_first |
| `20260110_223435_user_create_invalid_email` | 400 | === NAME === \| user_create_invalid_email |
| `20260110_223435_user_create_valid` | 201 | === NAME === \| user_create_valid |
| `20260110_223435_user_get_not_found` | 404 | === NAME === \| user_get_not_found |
---

## Automated Testing (pytest)

Automated testing was implemented using pytest in combination with Flask test_client(), allowing the API to be tested without running an external server. This approach ensures isolated, repeatable, and fast execution of test cases. The test suite validates both successful and failing scenarios across all implemented resources, including Users, Amenities, Places, and Reviews.

The automated tests were executed using the following command:
PYTHONPATH=hbnb python3 -m pytest -q

All automated tests completed successfully, with a total of 16 test cases passing without errors.

The test results confirm that the API consistently returns appropriate HTTP status codes and error messages. Requests targeting non-existent resources correctly return HTTP 404 Not Found responses using Flask-RESTx api.abort where applicable. Input validation is enforced through Flask-RESTx request schemas using @api.expect(..., validate=True), ensuring that malformed or incomplete payloads result in HTTP 400 Bad Request responses. The testing strategy does not require an external Flask server, which guarantees a clean testing environment and prevents side effects between test runs.

In conclusion, the automated testing process verifies that the HBnB API behaves as expected and complies with the specifications defined in Task 6. Validation logic, error handling, and response consistency are correctly implemented at the model, service, and API layers. The successful execution of all test cases demonstrates that the API is stable, well-documented through Swagger, and ready for future extensions and integration in subsequent development phases.
