## 1. User Registration

```mermaid
sequenceDiagram
    actor User
    participant API
    participant BL as BusinessLogic
    participant DB as Database

    User->>API: Register user (email, password)
    activate API

    API->>BL: Validate user data
    activate BL

    alt Valid data
        BL->>DB: Save user information
        activate DB
        DB-->>BL: Confirm save
        deactivate DB

        BL-->>API: Registration success
    else Invalid data
        BL-->>API: Validation error
    end

    deactivate BL

    API-->>User: Registration result (success/failure)
    deactivate API
