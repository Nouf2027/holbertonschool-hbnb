# Task 6 – Testing and Validation Report (HBnB Part 2)

## 1. Objective
The objective of this task is to implement validation rules for all entities
(**User**, **Place**, **Review**, **Amenity**), perform black-box testing using
cURL and Swagger (Flask-RESTx), and execute automated unit tests to ensure
correct API behavior.

---

## 2. Environment
- OS: Linux (Sandbox)
- Python: 3.x
- Framework: Flask + Flask-RESTx
- Storage: In-memory repository
- Base URL: http://127.0.0.1:5000
- Swagger URL: http://127.0.0.1:5000/api/v1/

---

## 3. Implemented Validation (Business Logic Layer)

### 3.1 User Validation
**Rules:**
- `first_name`: required, non-empty
- `last_name`: required, non-empty
- `email`: required, non-empty, valid email format

**Expected Behavior:**
- Invalid payload → **400 Bad Request**

---

### 3.2 Place Validation
**Rules:**
- `name` (title): required, non-empty
- `price_per_night`: must be a non-negative number
- `latitude`: must be between -90 and 90
- `longitude`: must be between -180 and 180
- `owner_id`: required and must reference an existing User

**Expected Behavior:**
- Invalid payload → **400 Bad Request**
- Non-existent `owner_id` → **404 Not Found**

---

### 3.3 Review Validation
**Rules:**
- `text`: required, non-empty
- `rating`: integer between 1 and 5
- `user_id`: required and must reference an existing User
- `place_id`: required and must reference an existing Place

**Expected Behavior:**
- Invalid payload → **400 Bad Request**
- Non-existent `user_id` or `place_id` → **404 Not Found**

---

### 3.4 Amenity Validation
**Rules:**
- `name`: required, non-empty

**Expected Behavior:**
- Invalid payload → **400 Bad Request**

---

## 4. Swagger Documentation Review (Flask-RESTx)

Swagger documentation was used as a reference to verify:
- Available API routes
- Request schemas and required fields
- Response formats and HTTP status codes

**Verified URL:**
- http://127.0.0.1:5000/api/v1/

**Namespaces Reviewed:**
- `/users`
- `/amenities`
- `/places`
- `/reviews`

---

## 5. Manual Black-Box Testing (cURL)

### 5.1 Swagger Availability
- **Request:** `GET /api/v1/`
- **Expected:** 200 OK
- **Result:** PASS

---

### 5.2 Users Endpoint
- Create User (valid) → **201 Created** → PASS  
- Create User (invalid email) → **400 Bad Request** → PASS  
- Create User (empty first_name) → **400 Bad Request** → PASS  
- Get User (not found) → **404 Not Found** → PASS  

---

### 5.3 Amenities Endpoint
- Create Amenity (valid) → **201 Created** → PASS  
- Create Amenity (empty name) → **400 Bad Request** → PASS  
- Get Amenity (not found) → **404 Not Found** → PASS  

---

### 5.4 Places Endpoint
- Create Place (missing name) → **400 Bad Request** → PASS  
- Create Place (invalid latitude) → **400 Bad Request** → PASS  
- Get Place (not found) → **404 Not Found** → PASS  

---

### 5.5 Reviews Endpoint
- Create Review (missing text) → **400 Bad Request** → PASS  
- Get Review (not found) → **404 Not Found** → PASS  

---

## 6. Automated Unit Tests (pytest)

### 6.1 Method
Automated tests were implemented using **pytest** with Flask `test_client()`.
This approach allows testing the API without running an external Flask server,
ensuring fast and isolated test execution.

### 6.2 Execution
```bash
PYTHONPATH=hbnb python3 -m pytest -q
