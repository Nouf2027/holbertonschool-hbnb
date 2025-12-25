## 1. User Registration

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant API
    participant BL as BusinessLogic
    participant DB as Database

    Note over User,API: Input: email, password

    User->>API: POST /users/register (email, password)
    activate API

    API->>BL: validateRegistration(email, password)
    activate BL

    BL->>BL: Check required fields\nValidate email format\nValidate password rules
    BL->>DB: findUserByEmail(email)
    activate DB
    DB-->>BL: userFound? (true/false)
    deactivate DB

    alt Valid data (not found + valid format)
        BL->>BL: Hash password\nBuild user object
        BL->>DB: saveUser(user)
        activate DB
        DB-->>BL: userId / success
        deactivate DB

        BL-->>API: success(userId)
    else Invalid data (found or invalid input)
        BL-->>API: error(message)
    end

    deactivate BL

    API-->>User: 201 Created OR 400 Bad Request
    deactivate API
