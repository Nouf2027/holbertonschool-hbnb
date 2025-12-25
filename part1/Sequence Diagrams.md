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
	


## 2. Place Creation

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant API
    participant BL as BusinessLogic
    participant DB as Database

    Note over User: User enters place details
    User->>API: Send place details
    activate API

    API->>BL: Check place details
    activate BL

    Note right of BL: Check required fields\nCheck place name format\nCheck location values

    BL->>DB: Check if place exists
    activate DB
    DB-->>BL: Place exists? (Yes / No)
    deactivate DB

    alt Place does not exist AND data is valid
        Note right of BL: Create new place object
        BL->>DB: Save new place
        activate DB
        DB-->>BL: Place saved (placeId)
        deactivate DB

        BL-->>API: Success (placeId)
        API-->>User: Place created
    else Place exists OR data is invalid
        BL-->>API: Failed (error)
        API-->>User: Error message
    end

    deactivate BL
    deactivate API
```
## Explanation

    -	 The user enters the place details (name, location, etc.).
	•	The API receives the place details from the user.
	•	The API sends the details to the Business Logic.
	•	The Business Logic checks:
	•	required fields,
	•	place name format,
	•	location values,
	•	and whether the place already exists.
	•	If the data is valid and the place does not exist:
	•	the place is saved in the database,
	•	a success message is returned to the user.
	•	If the place exists or the data is invalid:
	•	an error message is returned to the user.
-
	## 3. Review submission

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant API
    participant BL as BusinessLogic
    participant DB as Database

    Note over User: User writes a review and rating
    User->>API: Send review data
    activate API

    API->>BL: Check review data
    activate BL

    Note right of BL: Check required fields\nCheck rating value\nCheck user permission

    BL->>DB: Check if place exists
    activate DB
    DB-->>BL: Place exists? (Yes / No)
    deactivate DB

    alt Place exists AND data is valid
        Note right of BL: Create review object
        BL->>DB: Save review
        activate DB
        DB-->>BL: Review saved
        deactivate DB

        BL-->>API: Success
        API-->>User: Review created
    else Place not found OR data invalid
        BL-->>API: Failed
        API-->>User: Error message
    end

    deactivate BL
    deactivate API
```
# Explanation
	•	The user writes a review and gives a rating for a place.
	•	The API receives the review information from the user.
	•	The API sends the data to the Business Logic layer.
	•	The Business Logic checks:
	•	that all required fields are filled,
	•	that the rating value is valid,
	•	that the user is allowed to add a review,
	•	and that the place exists.
	•	If the data is valid and the place exists:
	•	the review is saved in the database,
	•	a success message is sent back to the user.
	•	If the data is invalid or the place does not exist:
	•	an error message is returned to the user.

# 4. Fetch Places
```mermaid
sequenceDiagram
    autonumber
    actor User
    participant API
    participant BL as BusinessLogic
    participant DB as Database

    Note over User: User wants to view available places
    User->>API: Request places list
    activate API

    API->>BL: Check request
    activate BL

    Note right of BL: Check request parameters\nCheck filters (if any)

    BL->>DB: Get places data
    activate DB
    DB-->>BL: List of places
    deactivate DB

    alt Places found
        BL-->>API: Send places list
        API-->>User: Display places
    else No places found
        BL-->>API: No data found
        API-->>User: Empty list message
    end

    deactivate BL
    deactivate API

```
# Explanation
	•	The user requests the list of places.
	•	The API sends the request to Business Logic.
	•	Business Logic checks parameters/filters and queries the database.
	•	If places are found, the list is returned to the user.
	•	If none are found, an empty list message is returned.
