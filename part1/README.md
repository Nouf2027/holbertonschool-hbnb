# Task 0: High-Level Package Diagram

## High-Level Package Diagram

```mermaid
classDiagram
direction TB

namespace "Presentation Layer" {
  class API_Routes
  class RequestHandlers
}

namespace "Business Logic Layer" {
  class HBnBFacade <<Facade>>
  class User
  class Place
  class Review
  class Amenity
}

namespace "Persistence Layer" {
  class Repositories
  class Storage <<database>>
}

API_Routes --> HBnBFacade : calls
RequestHandlers --> HBnBFacade : calls

HBnBFacade --> User : uses
HBnBFacade --> Place : uses
HBnBFacade --> Review : uses
HBnBFacade --> Amenity : uses

HBnBFacade --> Repositories : reads/writes
Repositories --> Storage : CRUD
```
## Explanatory Notes

### Presentation Layer (Services / API)
This layer represents the entry point of the application.
It handles user interactions and HTTP requests, and forwards all operations
to the Business Logic layer through the facade.

### Business Logic Layer (Models)
This layer contains the core business logic and the domain models
(User, Place, Review, Amenity).
The HBnBFacade provides a unified interface that is used by the Presentation layer
to access business operations.

### Persistence Layer
This layer is responsible for data storage and retrieval.
It interacts with the database through repositories or data access objects.

### Facade Pattern
The Facade pattern simplifies communication between layers by providing
a single entry point to the business logic.
It reduces coupling between components and improves the maintainability
and clarity of the system architecture.

