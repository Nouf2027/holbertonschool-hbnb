# Task 0: High-Level Package Diagram

## Objective
The objective of this task is to create a high-level package diagram that illustrates the three-layer architecture of the HBnB application and the communication between these layers using the Facade design pattern.

## Overview
The HBnB application follows a layered architecture that separates concerns into three main layers:
the Presentation Layer, the Business Logic Layer, and the Persistence Layer.
This design improves maintainability, scalability, and clarity of the system.

## High-Level Package Diagram

```mermaid
flowchart LR

subgraph Presentation_Layer [Presentation Layer]
    API[API / Services]
end

subgraph Business_Logic_Layer [Business Logic Layer]
    Facade[HBnBFacade]
    Models[User, Place, Review, Amenity]
end

subgraph Persistence_Layer [Persistence Layer]
    Repo[Repositories]
    DB[(Database)]
end

API --> Facade
Facade --> Models
Facade --> Repo
Repo --> DB
```
## Explanatory Notes

### Presentation Layer (Services / API)
This layer represents the entry point of the system.
It exposes API endpoints and services that handle client requests.
Requests are validated and forwarded to the Business Logic Layer through the Facade.

### Business Logic Layer (Models)
This layer contains the core business rules and domain models such as User, Place, Review, and Amenity.
It also includes the HBnBFacade, which acts as a unified interface between the Presentation Layer and the internal system components.

### Persistence Layer
This layer is responsible for data storage and retrieval.
It communicates with the database through repositories or data access objects.
This layer is accessed only by the Business Logic Layer.

### Facade Pattern
The Facade Pattern provides a single access point to the Business Logic Layer.
It simplifies communication between layers and hides internal implementation details.
This approach reduces coupling and improves maintainability, scalability, and clarity of the system architecture.

