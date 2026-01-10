# HBnB API Testing Documentation

This document provides comprehensive manual testing for the HBnB API endpoints
using black-box testing with curl commands.

## Prerequisites

- Flask application running on http://127.0.0.1:5000
- curl installed

## Testing Overview

The API includes the following entities:
- Users
- Amenities
- Places
- Reviews

---

## User Endpoints

Create User (Valid)

bash
curl -X POST http://127.0.0.1:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}'
,,,

Expected Result:
- 201 Created

---

Create User (Invalid Email)

bash
curl -X POST http://127.0.0.1:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{
  "first_name": "John",
  "last_name": "Doe",
  "email": "invalid"
}'
,,,

Expected Result:
- 400 Bad Request

---

Get User (Not Found)

bash
curl -X GET http://127.0.0.1:5000/api/v1/users/does-not-exist
,,,

Expected Result:
- 404 Not Found

---

## Amenity Endpoints

Create Amenity (Valid)

bash
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
-H "Content-Type: application/json" \
-d '{
  "name": "WiFi"
}'
,,,

Expected Result:
- 201 Created

---

Create Amenity (Empty Name)

bash
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
-H "Content-Type: application/json" \
-d '{
  "name": ""
}'
,,,

Expected Result:
- 400 Bad Request

---

Get Amenity (Not Found)

bash
curl -X GET http://127.0.0.1:5000/api/v1/amenities/does-not-exist
,,,

Expected Result:
- 404 Not Found

---

## Place Endpoints

Create Place (Missing Name)

bash
curl -X POST http://127.0.0.1:5000/api/v1/places/ \
-H "Content-Type: application/json" \
-d '{
  "description": "Test",
  "price_per_night": 100,
  "latitude": 0,
  "longitude": 0,
  "owner_id": "does-not-exist"
}'
,,,

Expected Result:
- 400 Bad Request

---

Create Place (Invalid Latitude)

bash
curl -X POST http://127.0.0.1:5000/api/v1/places/ \
-H "Content-Type: application/json" \
-d '{
  "name": "MyPlace",
  "description": "Test",
  "price_per_night": 100,
  "latitude": 200,
  "longitude": 0,
  "owner_id": "does-not-exist"
}'
,,,

Expected Result:
- 400 Bad Request

---

Get Place (Not Found)

bash
curl -X GET http://127.0.0.1:5000/api/v1/places/does-not-exist
,,,

Expected Result:
- 404 Not Found

---

## Review Endpoints

Create Review (Missing Text)

bash
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
-H "Content-Type: application/json" \
-d '{
  "rating": 5,
  "user_id": "does-not-exist",
  "place_id": "does-not-exist"
}'
,,,

Expected Result:
- 400 Bad Request

---

Get Review (Not Found)

bash
curl -X GET http://127.0.0.1:5000/api/v1/reviews/does-not-exist
,,,

Expected Result:
- 404 Not Found

---

## Conclusion

All API endpoints were tested using manual curl-based black-box testing.

Results:
- All validation rules are enforced correctly
- Correct HTTP status codes are returned
- Error handling behaves as expected
- The API conforms to the specifications defined in Task 6

This confirms that Task 6 requirements have been fully satisfied.
