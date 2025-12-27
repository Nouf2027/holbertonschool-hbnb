# HBnB Evolution — Technical Documentation


## 1. Introduction
This document describes the architecture and interaction flow of the HBNB Evolution project.
It explains how system components communicate using UML diagrams.
The document serves as a reference for understanding the system design.
 AUTHORS:
@Nouf2027
@
@
## 2. High-Level Architecture
The system follows a layered architecture.
The Presentation layer handles API requests.
The Business Logic layer contains application rules.
The Persistence layer is responsible for data storage.
 
## 3. Business Logic Layer
The Business Logic layer validates data and applies application rules.
It acts as a facade between the API and the database.
This layer ensures consistency and separation of concerns.

 ### 4.1 User Registration 

Purpose:
Create a new user account.

Flow:
- The user submits registration data.
- The API validates the input.
- The Business Logic checks rules and uniqueness.
- The user is saved in the database.

https://github.com/user-attachments/assets/3225190e-b1ff-462e-893d-541061bfb35d

 ### 4.2 Place Creation — POST /places

Purpose:
Create a new place.

Flow:
- The user submits place details.
- The system validates the data.
- The place is stored in the database.

https://github.com/user-attachments/assets/c73e51bb-d1f9-44d5-b894-07b7bd2b73aa

### 4.3 Review Submission — POST /places/{id}/reviews

Purpose:
Add a review to a place.

Flow:
- The user submits a review and rating.
- The system validates the request.
- The review is saved.

https://github.com/user-attachments/assets/3225190e-b1ff-462e-893d-541061bfb35d

### 4.4 Fetch Places — GET /places

Purpose:
Retrieve a list of available places.

Flow:
- The user requests places.
- Filters are validated if provided.
- A list of places is returned.

## 5. Conclusion
This document provides an overview of the system architecture and API interactions.
It helps understand how different components work together in the HBNB project.
