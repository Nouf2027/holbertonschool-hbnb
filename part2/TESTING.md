# Task 6 – Manual Testing Report (HBnB Part 2)

## Objective
This document describes the manual black-box testing performed on the HBnB API
using cURL to validate endpoint behavior, input validation, and HTTP status codes.

---

## Environment
- OS: Linux (Holberton Sandbox)
- Language: Python 3
- Framework: Flask + Flask-RESTx
- Storage: In-memory repository
- Base URL: http://127.0.0.1:5000
- Swagger UI: http://127.0.0.1:5000/api/v1/

---

## User Endpoints

### Create User (Valid)

Command:
    curl -X POST http://127.0.0.1:5000/api/v1/users/ \
    -H "Content-Type: application/json" \
    -d '{"first_name":"John","last_name":"Doe","email":"john.doe@example.com"}'

Expected Result:
- Status Code: 201 Created

Result:
- PASS

---

### Create User (Invalid Email)

Command:
    curl -X POST http://127.0.0.1:5000/api/v1/users/ \
    -H "Content-Type: application/json" \
    -d '{"first_name":"John","last_name":"Doe","email":"invalid"}'

Expected Result:
- Status Code: 400 Bad Request

Result:
- PASS

---

### Get User (Not Found)

Command:
    curl -X GET http://127.0.0.1:5000/api/v1/users/does-not-exist

Expected Result:
- Status Code: 404 Not Found

Result:
- PASS

---

## Amenity Endpoints

### Create Amenity (Valid)

Command:
    curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
    -H "Content-Type: application/json" \
    -d '{"name":"WiFi"}'

Expected Result:
- Status Code: 201 Created

Result:
- PASS

---

### Create Amenity (Empty Name)

Command:
    curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
    -H "Content-Type: application/json" \
    -d '{"name":""}'

Expected Result:
- Status Code: 400 Bad Request

Result:
- PASS

---

### Get Amenity (Not Found)

Command:
    curl -X GET http://127.0.0.1:5000/api/v1/amenities/does-not-exist

Expected Result:
- Status Code: 404 Not Found

Result:
- PASS

---

## Place Endpoints

### Create Place (Missing Name)

Command:
    curl -X POST http://127.0.0.1:5000/api/v1/places/ \
    -H "Content-Type: application/json" \
    -d '{"description":"Test","price_per_night":100,"latitude":0,"longitude":0,"owner_id":"does-not-exist"}'

Expected Result:
- Status Code: 400 Bad Request

Result:
- PASS

---

### Create Place (Invalid Latitude)

Command:
    curl -X POST http://127.0.0.1:5000/api/v1/places/ \
    -H "Content-Type: application/json" \
    -d '{"name":"MyPlace","description":"Test","price_per_night":100,"latitude":200,"longitude":0,"owner_id":"does-not-exist"}'

Expected Result:
- Status Code: 400 Bad Request

Result:
- PASS

---

### Get Place (Not Found)

Command:
    curl -X GET http://127.0.0.1:5000/api/v1/places/does-not-exist

Expected Result:
- Status Code: 404 Not Found

Result:
- PASS

---

## Review Endpoints

### Create Review (Missing Text)

Command:
    curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
    -H "Content-Type: application/json" \
    -d '{"rating":5,"user_id":"does-not-exist","place_id":"does-not-exist"}'

Expected Result:
- Status Code: 400 Bad Request

Result:
- PASS

---

### Get Review (Not Found)

Command:
    curl -X GET http://127.0.0.1:5000/api/v1/reviews/does-not-exist

Expected Result:
- Status Code: 404 Not Found

Result:
- PASS

---

## Conclusion
Manual cURL testing confirms that all HBnB API endpoints correctly enforce
validation rules, return appropriate HTTP status codes, and handle error
scenarios as expected. The implementation satisfies the requirements of Task 6.
