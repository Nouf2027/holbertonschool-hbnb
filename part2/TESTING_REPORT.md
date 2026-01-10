# Task 6 – Testing and Validation
HBnB Project – Part 2

## Overview
This document describes the testing and validation process for the HBnB REST API.
The goal of Task 6 is to verify that all implemented endpoints behave correctly,
handle validation rules properly, and return the expected HTTP status codes.

## Environment
- OS: Linux (Sandbox)
- Python: 3
- Framework: Flask + Flask-RESTx
- Data storage: In-memory repository
- Base URL: http://127.0.0.1:5000

## Swagger Documentation
Swagger documentation was reviewed to confirm that all endpoints are correctly exposed.

URL:
http://127.0.0.1:5000/api/v1/

Available namespaces:
- /users
- /amenities
- /places
- /reviews

## Testing Methodology
Testing was performed using:
- Manual black-box testing with curl
- Validation of required fields and boundary conditions
- Verification of HTTP status codes
- Logical flow testing between related entities

## User Endpoints Testing

### Create User (POST /api/v1/users/)
Valid case:
- first_name provided
- last_name provided
- email in valid format

Expected result:
- Status code: 201
- User object returned (without password)

Invalid cases:
- Empty first_name → 400
- Empty last_name → 400
- Invalid email format → 400
- Duplicate email → 400

### Get All Users (GET /api/v1/users/)
Expected result:
- Status code: 200
- List of users returned

### Get User by ID (GET /api/v1/users/<user_id>)
Valid case:
- Existing user ID → 200

Invalid case:
- Non-existent user ID → 404

### Update User (PUT /api/v1/users/<user_id>)
Valid case:
- Existing user ID with valid data → 200

Invalid case:
- Non-existent user ID → 404

## Amenity Endpoints Testing

### Create Amenity (POST /api/v1/amenities/)
Valid case:
- name provided and non-empty

Expected result:
- Status code: 201

Invalid cases:
- Empty name → 400
- Name too long → 400

### Get All Amenities (GET /api/v1/amenities/)
Expected result:
- Status code: 200

### Get Amenity by ID (GET /api/v1/amenities/<amenity_id>)
Valid case:
- Existing amenity ID → 200

Invalid case:
- Non-existent amenity ID → 404

### Update Amenity (PUT /api/v1/amenities/<amenity_id>)
Valid case:
- Existing amenity ID → 200

Invalid case:
- Non-existent amenity ID → 404

## Place Endpoints Testing

### Create Place (POST /api/v1/places/)
Valid case:
- title provided
- price is positive
- latitude between -90 and 90
- longitude between -180 and 180
- owner_id exists

Expected result:
- Status code: 201

Invalid cases:
- Missing title → 400
- Negative price → 400
- Latitude out of range → 400
- Longitude out of range → 400
- Non-existent owner_id → 404

### Get All Places (GET /api/v1/places/)
Expected result:
- Status code: 200

### Get Place by ID (GET /api/v1/places/<place_id>)
Valid case:
- Existing place ID → 200

Invalid case:
- Non-existent place ID → 404

### Update Place (PUT /api/v1/places/<place_id>)
Valid case:
- Existing place ID → 200

Invalid case:
- Non-existent place ID → 404

## Review Endpoints Testing

### Create Review (POST /api/v1/reviews/)
Valid case:
- text provided and non-empty
- rating between 1 and 5
- user_id exists
- place_id exists

Expected result:
- Status code: 201

Invalid cases:
- Empty text → 400
- Rating less than 1 → 400
- Rating greater than 5 → 400
- Non-existent user_id → 404
- Non-existent place_id → 404

### Get All Reviews (GET /api/v1/reviews/)
Expected result:
- Status code: 200

### Get Review by ID (GET /api/v1/reviews/<review_id>)
Valid case:
- Existing review ID → 200

Invalid case:
- Non-existent review ID → 404

### Update Review (PUT /api/v1/reviews/<review_id>)
Valid case:
- Existing review ID → 200

Invalid case:
- Non-existent review ID → 404

### Delete Review (DELETE /api/v1/reviews/<review_id>)
Valid case:
- Existing review ID → 204

Invalid case:
- Non-existent review ID → 404

## Validation Summary

### User Validation
- first_name required
- last_name required
- email required, valid format, unique

### Amenity Validation
- name required
- name length limited

### Place Validation
- title required
- price must be positive
- latitude range enforced
- longitude range enforced
- owner must exist

### Review Validation
- text required
- rating between 1 and 5
- user must exist
- place must exist

## Conclusion
All endpoints were reviewed and validated according to the project requirements.
The API correctly enforces validation rules, returns appropriate HTTP status codes,
and follows the expected behavior for both valid and invalid requests.
