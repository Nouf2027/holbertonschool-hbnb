# Task 6 - Testing & Validation Report

## Environment
- OS: Linux (sandbox)
- Python: 3.x
- Framework: Flask + Flask-RESTx
- Run command: (اكتبي الأمر اللي تشغلون فيه السيرفر)

## Swagger Verification
- URL: http://127.0.0.1:5000/api/v1/
- Verified namespaces:
  - /places
  - /reviews

## Manual Tests (cURL)
Used script: `./test_task6_curl.sh`

### Places
- POST /api/v1/places/ (valid) -> Expected 201
- POST /api/v1/places/ (invalid: missing title) -> Expected 400
- GET /api/v1/places/ -> Expected 200
- GET /api/v1/places/does-not-exist -> Expected 404

### Reviews
- POST /api/v1/reviews/ (invalid: missing text) -> Expected 400
- GET /api/v1/reviews/ -> Expected 200
- GET /api/v1/reviews/does-not-exist -> Expected 404
- GET /api/v1/places/does-not-exist/reviews -> Expected 404

## Automated Tests (unittest)
Command:
`python3 -m unittest discover -s tests -p "test_*.py" -v`

Test file:
- tests/test_reviews_places.py

## Validation Summary
- Place: required fields + range checks (حسب validate عندكم)
- Review: text required, rating 1..5, user exists, place exists
