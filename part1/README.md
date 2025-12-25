# Task 0: High-Level Package Diagram

## Objective
This diagram provides a high-level overview of the three-layer architecture of the HBnB application and shows how the layers communicate using the Facade design pattern.

## High-Level Package Diagram

```mermaid
classDiagram
direction TB

namespace PresentationLayer {
  class ServicesAPI {
    <<Interface>>
    +handle_request()
    +send_response()
  }

  class UserAPI {
    +register()
    +update_profile()
    +delete()
  }

  class PlaceAPI {
    +create()
    +update()
    +delete()
    +list()
  }

  class ReviewAPI {
    +create()
    +update()
    +delete()
    +list_by_place()
  }

  class AmenityAPI {
    +create()
    +update()
    +delete()
    +list()
  }
}

namespace BusinessLogicLayer {
  class HBnBFacade {
    <<Facade>>
    +register_user()
    +update_user()
    +delete_user()

    +create_place()
    +update_place()
    +delete_place()
    +list_places()

    +create_review()
    +update_review()
    +delete_review()
    +list_reviews_by_place()

    +create_amenity()
    +update_amenity()
    +delete_amenity()
    +list_amenities()
  }

  class User
  class Place
  class Review
  class Amenity
}

namespace PersistenceLayer {
  class UserRepository {
    +save()
    +find_by_id()
    +find_by_email()
    +update()
    +delete()
  }

  class PlaceRepository {
    +save()
    +find_by_id()
    +find_all()
    +update()
    +delete()
  }

  class ReviewRepository {
    +save()
    +find_by_id()
    +find_by_place_id()
    +update()
    +delete()
  }

  class AmenityRepository {
    +save()
    +find_by_id()
    +find_all()
    +update()
    +delete()
  }
}

ServicesAPI --> UserAPI
ServicesAPI --> PlaceAPI
ServicesAPI --> ReviewAPI
ServicesAPI --> AmenityAPI

UserAPI --> HBnBFacade : Facade
PlaceAPI --> HBnBFacade : Facade
ReviewAPI --> HBnBFacade : Facade
AmenityAPI --> HBnBFacade : Facade

HBnBFacade --> UserRepository
HBnBFacade --> PlaceRepository
HBnBFacade --> ReviewRepository
HBnBFacade --> AmenityRepository
```
## Explanatory Notes

### Presentation Layer (Services / API)
This layer represents the entry point of the system.
It exposes API endpoints and services that receive client requests and forward them to the Business Logic layer through the facade.

### Business Logic Layer (Models)
This layer contains the core business rules and the domain models, including User, Place, Review, and Amenity.
The HBnBFacade provides a unified interface that is used by the Presentation layer to interact with the business logic.

### Persistence Layer
This layer is responsible for data storage and retrieval.
It interacts directly with the database through repositories, abstracting database operations from the business logic.

### Facade Pattern
The Facade pattern simplifies communication between the Presentation and Business Logic layers by providing a single access point to the system’s core functionality.
This approach reduces coupling between components and improves the maintainability and clarity of the application architecture.

