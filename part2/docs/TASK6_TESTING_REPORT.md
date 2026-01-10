# Task 6 – Testing and Validation Report (HBnB Part 2)

## 1) Objective
Implement validation rules for all entities (User, Place, Review, Amenity),
perform black-box testing using cURL and Swagger (Flask-RESTx),
and provide automated unit tests to validate API behavior.

## 2) Environment
- OS: Linux (Sandbox)
- Python: 3.x
- Framework: Flask + Flask-RESTx
- Storage: In-memory repository
- Base URL: http://127.0.0.1:5000
- Swagger URL: http://127.0.0.1:5000/api/v1/

## 3) Implemented Validation (Business Logic Layer)

### 3.1 User Validation
Rules:
- first_name: required, non-empty
- last_name: required, non-empty
- email: required, non-empty, valid email format

Expected behavior:
- Invalid payload -> 400 Bad Request

### 3.2 Place Validation
Rules:
- name (title): required, non-empty
- price_per_night: must be >= 0
- latitude: must be between -90 and 90
- longitude: must be between -180 and 180
- owner_id: required and must reference an existing User

Expected behavior:
- Invalid payload -> 400 Bad Request
- owner_id not found -> 404 Not Found

### 3.3 Review Validation
Rules:
- text: required, non-empty
- rating: integer between 1 and 5
- user_id: required and must reference an existing User
- place_id: required and must reference an existing Place

Expected behavior:
- Invalid payload -> 400 Bad Request
- user_id or place_id not found -> 404 Not Found

### 3.4 Amenity Validation
Rules:
- name: required, non-empty

Expected behavior:
- Invalid payload -> 400 Bad Request

## 4) Swagger Documentation Review (Flask-RESTx)
Swagger was used as the reference for:
- Available routes
- Request schemas (required fields)
- Response formats and status codes

Verified URL:
- http://127.0.0.1:5000/api/v1/

Namespaces verified:
- /users
- /amenities
- /places
- /reviews

## 5) Manual Black-Box Testing (cURL)

### 5.1 Swagger Availability
Request:
- GET /api/v1/

Expected:
- 200 OK (Swagger UI page)

Result:
- PASS (200 OK)

### 5.2 Users Endpoint Tests

#### Create User (Valid)
Request:
- POST /api/v1/users/
Payload:
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}

Expected:
- 201 Created

Result:
- PASS (201 Created)

#### Create User (Invalid Email)
Request:
- POST /api/v1/users/
Payload:
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "invalid"
}

Expected:
- 400 Bad Request

Result:
- PASS (400 Bad Request)

#### Create User (Empty first_name)
Request:
- POST /api/v1/users/
Payload:
{
  "first_name": "",
  "last_name": "Doe",
  "email": "x@y.com"
}

Expected:
- 400 Bad Request

Result:
- PASS (400 Bad Request)

#### Get User (Not Found)
Request:
- GET /api/v1/users/does-not-exist

Expected:
- 404 Not Found

Result:
- PASS (404 Not Found)

### 5.3 Amenities Endpoint Tests

#### Create Amenity (Valid)
Request:
- POST /api/v1/amenities/
Payload:
{
  "name": "WiFi"
}

Expected:
- 201 Created

Result:
- PASS (201 Created)

#### Create Amenity (Empty name)
Request:
- POST /api/v1/amenities/
Payload:
{
  "name": ""
}

Expected:
- 400 Bad Request

Result:
- PASS (400 Bad Request)

#### Get Amenity (Not Found)
Request:
- GET /api/v1/amenities/does-not-exist

Expected:
- 404 Not Found

Result:
- PASS (404 Not Found)

### 5.4 Places Endpoint Tests

#### Create Place (Missing name/title)
Request:
- POST /api/v1/places/
Payload:
{
  "description": "Test",
  "price_per_night": 100,
  "latitude": 0,
  "longitude": 0,
  "owner_id": "does-not-exist"
}

Expected:
- 400 Bad Request

Result:
- PASS (400 Bad Request)

#### Create Place (Invalid latitude)
Request:
- POST /api/v1/places/
Payload:
{
  "name": "MyPlace",
  "description": "Test",
  "price_per_night": 100,
  "latitude": 200,
  "longitude": 0,
  "owner_id": "does-not-exist"
}

Expected:
- 400 Bad Request

Result:
- PASS (400 Bad Request)

#### Get Place (Not Found)
Request:
- GET /api/v1/places/does-not-exist

Expected:
- 404 Not Found

Result:
- PASS (404 Not Found)

### 5.5 Reviews Endpoint Tests

#### Create Review (Missing text)
Request:
- POST /api/v1/reviews/
Payload:
{
  "rating": 5,
  "user_id": "does-not-exist",
  "place_id": "does-not-exist"
}

Expected:
- 400 Bad Request (schema validation / missing required field)

Result:
- PASS (400 Bad Request)

#### Get Review (Not Found)
Request:
- GET /api/v1/reviews/does-not-exist

Expected:
- 404 Not Found

Result:
- PASS (404 Not Found)

## 6) Automated Unit Tests (pytest)

### 6.1 Method
Automated tests were implemented using `pytest` with Flask `test_client()`.
This approach tests the Flask application directly without requiring a running external server,
resulting in fast, isolated, and repeatable test execution.

### 6.2 Execution
Command:
```bash
PYTHONPATH=hbnb python3 -m pytest -q
## 6. Results

✅ All tests passed successfully.

**Total:** 16 passed

---

## 6.3 Notes / Edge Cases

- For non-existent resources, the API consistently returns **404 Not Found** with a clear error message,  
  using Flask-RESTx `api.abort()` where applicable.

- Request payload validation relies on Flask-RESTx schemas  
  (`@api.expect(..., validate=True)`), ensuring that missing required fields return  
  **400 Bad Request** responses.

- No external Flask server is required during unit testing, ensuring stable, fast,  
  and isolated test execution.

---

## 7. Conclusion

Task 6 requirements were completed successfully:

- Validation rules were implemented for **User**, **Place**, **Review**, and **Amenity** entities.
- Swagger documentation was used to verify API routes and request/response schemas.
- Manual black-box testing using **cURL** confirmed correct behavior and HTTP status codes.
- Automated unit tests validated both valid and invalid scenarios, with all tests passing  
  successfully (**16 passed**).

Overall, the API endpoints behave as expected and consistently enforce validation rules.

