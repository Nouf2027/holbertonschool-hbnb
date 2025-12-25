## 1. User Registration

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant API
    participant BL as Business Logic
    participant DB as Database

    Note over User,API: User enters email and password

    User->>API: Send registration data
    activate API

    API->>BL: Check registration data
    activate BL

    Note right of BL: 
    - Check required fields
    - Check email format
    - Check password rules

    BL->>DB: Check if user exists
    activate DB
    DB-->>BL: User exists? (Yes / No)
    deactivate DB

    alt User does not exist and data is valid
        BL->>DB: Save new user
        activate DB
        DB-->>BL: User saved
        deactivate DB

        BL-->>API: Registration successful
        API-->>User: Account created
    else User exists or data is invalid
        BL-->>API: Registration failed
        API-->>User: Error message
    end

    deactivate BL
    deactivate API
