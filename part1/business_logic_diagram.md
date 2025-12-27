# Business Logic Layer Diagram

## This diagram represents the business logic layer of the HBnB system.
It shows the main entities, their attributes, methods, and relationships.






<img src="https://github.com/user-attachments/assets/55936c0c-c09b-4901-b95b-f047a4c62b89" width="100%" />





## Explanatory Notes

## User
Represents a person who uses the HBnB system, either as a host or a guest.

Role:
The User is responsible for creating and managing places and for writing reviews on places created by other users.

Attributes: 
The User entity includes identifying and account-related information such as id, email, first_name, last_name, and timestamps for creation and updates.

Methods:
The User can write reviews for places and create new places in the system



## Place
Represents a property or accommodation that is listed in the HBnB system.

Role:
The Place acts as the central business entity. It is owned by a user, can receive multiple reviews, and can be associated with multiple amenities.

Attributes:
The Place contains descriptive and pricing information such as id, owner_id, description, creattion date, price_per_night.

Methods: 
The Place allows adding reviews and associating amenities to describe available features.



