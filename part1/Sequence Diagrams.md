## 1. User Registration

```mermaid 
sequenceDiagram
    autonumber
    actor User
    participant API
    participant BL as BusinessLogic
    participant DB as Database

    Note over User,API: User enters email and password

    User->>API: Send registration data
    activate API

    API->>BL: Check registration data
    activate BL

    Note right of BL: Check required fields \n Check email format \n Check password rules

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
```
# Explanation

	-	The user enters an email and password to create a new account.
	-	The API receives the registration data from the user.
	-	The API sends the data to the Business Logic layer for checking.
	-	The Business Logic checks:
	-	if all required fields are filled,
	-	if the email format is correct,
	-	if the password follows the rules.
	-	The Business Logic asks the Database if the user already exists.

If the data is valid and the user does not exist:

	-	The Business Logic saves the new user in the Database.
	-	The Database confirms that the user is saved.
	-	A success message is returned to the user.

If the data is invalid or the user already exists:

	-	An error message is returned to the user.



