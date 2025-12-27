## HBnB Evolution — Technical Documentation
# Introduction
This document provides the technical documentation for the HBnB Evolution project.
It describes the system architecture, business logic design, and API interaction
flows using UML diagrams. The document serves as a reference for the implementation
phases of the project.

AUTHORS :

# High-Level Architecture
The application follows a layered architecture consisting of three main layers:

- Presentation Layer: Handles user interaction through the API.
- Business Logic Layer: Contains the core application logic and entities.
- Persistence Layer: Responsible for data storage and retrieval.

Communication between layers is handled using the Facade pattern to ensure
loose coupling and separation of concerns.

# Business Logic Layer
The Business Logic layer includes the core entities of the system such as User,
Place, Review, and Amenity. Each entity contains attributes and methods that
represent the business rules of the application.

Relationships between entities reflect real-world interactions, such as users
owning places and reviews being associated with both users and places.

# API Interaction Flow (Sequence Diagrams)
Purpose:
This sequence diagram illustrates the process of submitting a review.

Participants:
- User
- API
- BusinessLogic

Main Flow:
1. The user submits a review and rating.
2. The API receives the request.
3. The API forwards the data to the BusinessLogic.
4. The BusinessLogic validates the data.
5. The review is created and saved.
6. A success response is returned to the user.

Alternative Flow:
- If the place does not exist or the data is invalid, an error message is returned.


  This design ensures separation of concerns between layers.
The use of the Facade pattern simplifies communication between the API
and the Business Logic layer while maintaining flexibility and scalability.
