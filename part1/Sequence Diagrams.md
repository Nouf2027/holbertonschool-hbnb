
# Sequence Diagrams for API Calls
<img width="3004" height="1284" alt="image" src="https://github.com/user-attachments/assets/9520d33e-5460-48eb-8441-c2450f7027e3" />

## Explanation

 - The user sends registration information to the API.
 - The API forwards the request to the business logic layer for validation.
 - The business logic stores the user data in the database.
 - A confirmation is returned back through the layers to the user.
<img width="3004" height="1348" alt="image" src="https://github.com/user-attachments/assets/1a967759-527d-4328-ab95-81faea583e92" />

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


sequenceDiagram
    autonumber
    actor User
    participant API
    participant BL as BusinessLogic
    participant DB as Database

    User->>API: Register User (email, password, etc.)
    API->>BL: Validate & process registration
    BL->>BL: Check required fields + password rules

    alt Invalid data
        BL-->>API: Validation failed (400)
        API-->>User: Registration failed (error message)
    else Valid data
        BL->>DB: Store user data
        DB-->>BL: Confirm save
        BL-->>API: Return success (201)
        API-->>User: Registration successful
    end
