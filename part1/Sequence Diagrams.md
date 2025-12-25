
# Sequence Diagrams for API Calls



# Sequence Diagrams for API Calls

## 1. User Registration

```mermaid
sequenceDiagram
    actor User
    participant API
    participant BL as BusinessLogic
    participant DB as Database

    User->>API: Register user (email, password)
    API->>BL: Validate and process input

    alt Valid input
        BL->>DB: Store user data
        DB-->>BL: Confirm save
        BL-->>API: Success
        API-->>User: Registration successful
    else Invalid input
        BL-->>API: Validation error
        API-->>User: Registration failed
    end

## Explanation

 - The user submits place information.
 - The request is validated and processed.
 - The place is stored in the database.
 - A response is returned indicating success or failure.
   <img width="1350" height="552" alt="image" src="https://github.com/user-attachments/assets/7b6bbac1-debd-4c4f-8c20-139f481b735f" />

## Explanation

 - The user submits a review request to the system.
 - The API forwards the review data to the Business Logic layer for validation.
 - After validation, the review is stored in the database.
 - A confirmation is returned through the Business Logic to the API.
 - The API sends the final success or failure response back to the user.
   <img width="1302" height="392" alt="image" src="https://github.com/user-attachments/assets/b6643095-8d23-42d4-a6cb-dad4fda3efb2" />

## Explanation

 - The user sends a request to retrieve a list of places based on specific criteria.
 - The API receives the request and forwards it to the Business Logic layer for processing.
 - The Business Logic retrieves the relevant places from the database.
 - The retrieved data is sent back through the API and displayed to the user.


```mermaid
sequenceDiagram
    actor User
    participant API
    participant BL as BusinessLogic
    participant DB as Database

    User->>API: Register user
    API->>BL: Validate data
    BL->>DB: Save user
    DB-->>BL: Confirm save
    BL-->>API: Success
    API-->>User: Registration successful
```
