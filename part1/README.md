# HBnB Evolution — Technical Documentation

## Table of Contents
- [1. Introduction](#1-introduction)
- [2. High-Level Architecture](#2-high-level-architecture)
- [3. Business Logic Layer](#3-business-logic-layer)
- [4. API Interaction Flow](#4-api-interaction-flow)
  - [4.1 User Registration — POST /users](#41-user-registration--post-users)
  - [4.2 Place Creation — POST /places](#42-place-creation--post-places)
  - [4.3 Review Submission — POST /places/{id}/reviews](#43-review-submission--post-placesidreviews)
  - [4.4 Fetching a List of Places — GET /places](#44-fetching-a-list-of-places--get-places)
- [5. Design Decisions](#5-design-decisions)
- [6. Conclusion](#6-conclusion)
- [References](#references)

---

## 1. Introduction

This document provides the technical documentation for the **HBnB Evolution** project.  
It consolidates the UML diagrams and explanatory notes created in previous tasks into a single, well-structured reference.

The goal of this document is to:
- Describe the system architecture and the separation of concerns between layers.
- Present the core entities and relationships in the Business Logic layer.
- Explain how API requests flow through the system using sequence diagrams.

This document will be used as a **blueprint** for later implementation phases to ensure consistency, correctness, and maintainability.

---

## 2. High-Level Architecture

HBnB Evolution follows a **layered architecture** composed of three main layers:

### 2.1 Presentation Layer
- The entry point for users/clients.
- Exposes API endpoints and handles incoming requests.
- Performs basic request parsing and initial validation.
- Delegates operations to the Business Logic layer.

### 2.2 Business Logic Layer
- Contains the core application rules and workflows.
- Holds the main domain entities (User, Place, Review, Amenity).
- Validates business rules (required fields, uniqueness, rating ranges, relationships).
- Provides a **Facade** interface that the Presentation layer calls, to keep coupling low.

### 2.3 Persistence Layer
- Responsible for data storage and retrieval.
- Abstracts database access from the rest of the system.
- Ensures Business Logic does not directly depend on low-level storage details.

### 2.4 Communication Between Layers (Facade Pattern)
The **Facade** pattern is used to:
- Provide a clean and simplified interface for the Presentation layer.
- Centralize business operations in one point.
- Reduce tight coupling and make the system easier to evolve.

#### High-Level Package Diagram
![High-Level Package Diagram](./High-Level-Package-Diagram.png)

**Explanatory Notes (Package Diagram):**
- **Purpose:** Illustrates the three-layer architecture and how layers communicate using a Facade.
- **Key Components:** Presentation, BusinessLogic (Facade + Entities), Persistence.
- **Design Rationale:** Keeps responsibilities separated; Presentation does not directly access storage.
- **Fit in Overall Design:** Acts as the global map of the system before implementation.

---

## 3. Business Logic Layer

The Business Logic layer defines the core domain entities and how they interact.  
The main entities include: **User, Place, Review, Amenity**.

### 3.1 Core Entities

#### User
- Represents a person interacting with the system.
- Typical attributes: first_name, last_name, email, password, is_admin.
- Rules:
  - Email should be unique.
  - Required fields must be present.

#### Place
- Represents a property listing created by a user (owner).
- Typical attributes: title, description, price, latitude, longitude, owner_id.
- Rules:
  - A place is linked to one owner (User).
  - Required fields must be validated (title, price, location).

#### Review
- Represents feedback left by a user for a place.
- Typical attributes: rating, comment, user_id, place_id.
- Rules:
  - Rating must be within an accepted range (e.g., 1–5).
  - Review must reference an existing place and user.

#### Amenity
- Represents features that can be associated with a place (e.g., Wi-Fi, parking).
- Typical attributes: name, description.
- Rules:
  - Amenity can be associated with multiple places.

### 3.2 Relationships (High-Level)
- A **User** can create multiple **Places** (User 1 → * Place).
- A **Place** can have multiple **Reviews** (Place 1 → * Review).
- A **User** can write multiple **Reviews** (User 1 → * Review).
- A **Place** can have multiple **Amenities** and an Amenity can belong to multiple Places (* ↔ *).

#### Detailed Class Diagram (Business Logic Layer)
![Detailed Class Diagram](./Detailed-Class-Diagram.png)

**Explanatory Notes (Class Diagram):**
- **Purpose:** Shows the Business Logic entities, attributes, methods, and relationships.
- **Key Components:** User, Place, Review, Amenity, and the Facade interface.
- **Design Rationale:** Entities model the domain; relationships enforce consistency and guide APIs.
- **Fit in Overall Design:** Provides the internal blueprint for implementing models and business rules.

---

## 4. API Interaction Flow

This section explains how API calls move through the system layers:
1. Client sends request to **API (Presentation Layer)**.
2. API validates and forwards to **Business Logic (Facade)**.
3. Business Logic checks rules and interacts with **Persistence**.
4. System returns a success/error response back to the client.

---

### 4.1 User Registration — POST /users

**Purpose:**  
Create a new user account.

**Flow:**
- The client submits registration data.
- The API validates the input format (required fields).
- Business Logic checks business rules and ensures the user does not already exist.
- Persistence stores the new user.
- A success response is returned to the client.

![User Registration Sequence Diagram](./user_registration.png)

**Explanatory Notes:**
- **Key components:** Client, API, BusinessLogic (Facade), Persistence/Database.
- **Design decision:** Business Logic handles uniqueness and rules; API only does basic validation.
- **Alternative flow:** If user exists or data is invalid, return an error message.

---

### 4.2 Place Creation — POST /places

**Purpose:**  
Create a new place listing.

**Flow:**
- The user submits place details.
- The API forwards the request to Business Logic after basic validation.
- Business Logic validates required fields, checks place constraints, and verifies it does not already exist.
- Persistence stores the new place and returns its identifier.
- A success response (with placeId) is returned.

![Place Creation Sequence Diagram](./place_creation.png)

**Explanatory Notes:**
- **Key components:** Client, API, BusinessLogic, Persistence.
- **Design decision:** All domain rules (title format, location values) live in Business Logic.
- **Alternative flow:** If the place exists or data is invalid, return an error response.

---

### 4.3 Review Submission — POST /places/{id}/reviews

**Purpose:**  
Submit a review and rating for a place.

**Flow:**
- The user submits review data (rating + comment).
- The API forwards the request to Business Logic.
- Business Logic validates fields, validates rating range, and checks that the place exists.
- The review object is created and stored.
- A success response is returned.

![Review Submission Sequence Diagram](./review_submission.png)

**Explanatory Notes:**
- **Key components:** Client, API, BusinessLogic, Persistence.
- **Design decision:** Place existence and rating rules are enforced in Business Logic.
- **Alternative flow:** If place not found or data invalid, return an error message.

---

### 4.4 Fetching a List of Places — GET /places

**Purpose:**  
Retrieve available places (optionally using filters).

**Flow:**
- The user requests the list of places.
- The API forwards request parameters to Business Logic.
- Business Logic validates request parameters and applies filters if present.
- Persistence retrieves the list from storage.
- The API returns the results to the user.

![Fetch Places Sequence Diagram](./fetch_places.png)

**Explanatory Notes:**
- **Key components:** Client, API, BusinessLogic, Persistence.
- **Design decision:** Filtering/validation lives in Business Logic for consistency.
- **Alternative flow:** If no results exist, return an empty list response.

---

## 5. Design Decisions

### 5.1 Layered Architecture
Separating Presentation, Business Logic, and Persistence ensures:
- Clear responsibilities (Separation of Concerns).
- Easier testing and maintenance.
- Flexibility to change storage later without changing business rules.

### 5.2 Facade Pattern
Using a Facade between Presentation and Business Logic:
- Reduces coupling between layers.
- Provides a single entry point for business operations.
- Keeps API controllers thinner and more readable.

### 5.3 UML as a Reference
UML diagrams are used to:
- Standardize communication of design.
- Provide a reference for implementation.
- Ensure consistency between requirements and code.

---

## 6. Conclusion

This document compiles the architecture, core domain design, and API interaction flows of **HBnB Evolution**.  
It serves as a reference architecture and should be used throughout implementation to maintain consistency, correctness, and maintainability.

---

## References
- UML Diagrams Overview
- Facade Design Pattern
- REST API Design Guidelines
 layer while maintaining flexibility and scalability.
