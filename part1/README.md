# Task 0: High-Level Package Diagram (HBnB)

## High-Level Package Diagram 

```mermaid
classDiagram
direction LR

%% =========================
%% Presentation Layer
%% =========================
namespace presentation {
  class API {
    <<Service>>
    +handleRequest()
  }

  class Services {
    <<Service>>
    +validateInput()
    +formatResponse()
  }
}

%% =========================
%% Business Logic Layer
%% =========================
namespace business {
  class HBnBFacade {
    <<Facade>>
    +createUser()
    +createPlace()
    +createReview()
    +listAmenities()
  }

  class User
  class Place
  class Review
  class Amenity
}

%% =========================
%% Persistence Layer
%% =========================
namespace persistence {
  class Repository {
    <<Repository>>
    +save()
    +getById()
    +list()
    +delete()
  }

  class Database {
    <<Database>>
  }
}

%% =========================
%% Relationships / Communication
%% =========================

presentation.API --> presentation.Services : uses
presentation.Services --> business.HBnBFacade : calls (Facade)

business.HBnBFacade --> business.User : manages
business.HBnBFacade --> business.Place : manages
business.HBnBFacade --> business.Review : manages
business.HBnBFacade --> business.Amenity : manages

business.HBnBFacade --> persistence.Repository : data access
persistence.Repository --> persistence.Database : CRUD
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

