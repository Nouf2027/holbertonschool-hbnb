## 1. User Registration

```mermaid
sequenceDiagram
    autonumber
    actor U as User
    participant API
    participant BL as Business Logic
    participant DB as Database

    Note over U,API: Input: email + password

    U->>API: POST /users/register
    activate API

    API->>BL: validateRegistration(email, password)
    activate BL

    Note right of BL: 1) Check required fields\n2) Validate email format\n3) Validate password rules

    BL->>DB: findUserByEmail(email)
    activate DB
    DB-->>BL: userFound? (true/false)
    deactivate DB

    alt user not found AND data valid
        BL->>BL: hashPassword()
        BL->>DB: saveUser(user)
        activate DB
        DB-->>BL: saved (userId)
        deactivate DB

        BL-->>API: success(userId)
        API-->>U: 201 Created
    else user exists OR invalid input
        BL-->>API: error(message)
        API-->>U: 400 Bad Request
    end

    deactivate BL
    deactivate API
