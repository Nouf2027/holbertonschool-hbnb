# HBnB – Part 2: Business Logic & API

## Project Overview

This part of the **HBnB** project focuses on implementing the **Business Logic layer** and building the **Presentation layer (REST API)** using **Flask** and **Flask-RESTx**.

The application follows a **three-layer architecture** to ensure clear separation of concerns, maintainability, and testability.

### Architecture Layers
- **Presentation Layer**: REST API built with Flask-RESTx
- **Business Logic Layer**: Core models and rules exposed via a Facade
- **Persistence Layer**: In-memory repository

---

## Implemented Tasks

### Task 0 – Project Setup
- Modular project structure
- Flask application factory
- In-memory repository
- Facade pattern to decouple API from business logic

---

### Task 1 – Core Business Logic
Implemented the following domain models:

- **User**
- **Place**
- **Review**
- **Amenity**

All models inherit from a shared **BaseModel** that provides:
- UUID identifier
- Creation and update timestamps
- Serialization support

---

### Task 2 – User Endpoints
Implemented REST endpoints for users:

- `POST /api/v1/users/`
- `GET /api/v1/users/`
- `GET /api/v1/users/<user_id>`
- `PUT /api/v1/users/<user_id>`

Validations:
- Email uniqueness
- Required fields validation

Notes:
- Passwords are never exposed in API responses

---

### Task 3 – Amenity Endpoints
Implemented REST endpoints for amenities:

- `POST /api/v1/amenities/`
- `GET /api/v1/amenities/`
- `GET /api/v1/amenities/<amenity_id>`
- `PUT /api/v1/amenities/<amenity_id>`

Notes:
- DELETE operation is intentionally not implemented

---

### Task 4 – Place Endpoints
Implemented REST endpoints for places:

- `POST /api/v1/places/`
- `GET /api/v1/places/`
- `GET /api/v1/places/<place_id>`
- `PUT /api/v1/places/<place_id>`

Validations:
- Title must not be empty
- Price must be a positive number
- Latitude must be between -90 and 90
- Longitude must be between -180 and 180

Notes:
- DELETE operation is not implemented

---

### Task 5 – Review Endpoints
Implemented REST endpoints for reviews:

- `POST /api/v1/reviews/`
- `GET /api/v1/reviews/`
- `GET /api/v1/reviews/<review_id>`
- `PUT /api/v1/reviews/<review_id>`
- `DELETE /api/v1/reviews/<review_id>`

Additional endpoints:
- `GET /api/v1/places/<place_id>/reviews`

Validations:
- Review text must not be empty
- Rating must be an integer between 1 and 5
- `user_id` and `place_id` are required
- Proper handling of non-existent resources (404)

---

### Task 6 – Testing and Validation

Implemented comprehensive testing and validation for all endpoints.

#### Validation
- Validation logic implemented at the model and facade levels
- Proper HTTP status codes returned for invalid input and missing resources

#### Manual Testing
- Black-box testing performed using `cURL`
- Swagger documentation used to verify request/response formats

A dedicated script is provided:
- `run_task6.sh` – Executes all manual API tests and saves outputs

#### Automated Testing
- Automated black-box tests implemented using `unittest`
- Tests cover:
  - Valid requests
  - Invalid input
  - Boundary cases
  - Non-existent resources

Test files:
- `tests/test_endpoints_blackbox.py`

#### Testing Documentation
- Detailed testing report provided:
  - `TESTING_REPORT.md`
- All test outputs stored under:
  - `reports/`

---

## Technologies Used
- Python 3
- Flask
- Flask-RESTx
- unittest
- cURL

---

## How to Run the Application

From the `part2/` directory:

```bash
python3 hbnb/run.py



