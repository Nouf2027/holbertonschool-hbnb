# HBnB - Part 2

## Project Overview
This part of the HBnB project focuses on implementing the **Business Logic layer** and building the **Presentation layer (API)** using **Flask** and **Flask-RESTx**.

The project follows a **three-layer architecture**:
- **Presentation Layer** (API endpoints with Flask-RESTx)
- **Business Logic Layer** (Models + Facade)
- **Persistence Layer** (In-memory repository)

## Implemented Tasks

### Task 0 – Project Setup
- Modular project structure
- Flask application factory
- In-memory repository
- Facade pattern setup

### Task 1 – Core Business Logic
- User
- Place
- Review
- Amenity
- Shared BaseModel with UUID and timestamps

### Task 2 – User Endpoints
- `POST /api/v1/users/` (create user with email uniqueness check)
- `GET /api/v1/users/` (list users)
- `GET /api/v1/users/<user_id>` (get user by id)
- `PUT /api/v1/users/<user_id>` (update user)
- Password is not returned in API responses
### Task 3 – Amenity Endpoints

- POST /api/v1/amenities/ (create amenity)
- GET /api/v1/amenities/ (list amenities)
- GET /api/v1/amenities/<amenity_id> (get amenity by id)
- PUT /api/v1/amenities/<amenity_id> (update amenity)
- DELETE operation is not implemented for amenities
  
## Technologies Used
- Python 3
- Flask
- Flask-RESTx

## How to Run
From the `part2/` directory:

```bash
pip3 install -r hbnb/requirements.txt
python3 hbnb/run.py

