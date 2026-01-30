from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # ================= USERS =================
    def create_user(self, user_data):
        if not user_data:
            return None, "No input data provided"

        
        password = (user_data.get("password") or "").strip()
        if not password:
            return None, "Missing password"

        user = User(**user_data)  # password gets hashed in the User model
        valid, error = user.validate()
        if not valid:
            return None, error

        if self.get_user_by_email(user.email):
            return None, "Email already exists"

        self.user_repo.add(user)
        return user, None

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        if not user:
            return None, "User not found"

        if not data:
            return None, "No input data provided"

        if "first_name" in data:
            user.first_name = (data.get("first_name") or "").strip()
        if "last_name" in data:
            user.last_name = (data.get("last_name") or "").strip()
        if "email" in data:
            new_email = (data.get("email") or "").strip()
            if new_email != user.email and self.get_user_by_email(new_email):
                return None, "Email already exists"
            user.email = new_email

        valid, error = user.validate()
        if not valid:
            return None, error

        return user, None

    # ================= AMENITIES =================
    def create_amenity(self, data):
        if not data:
            return None, "No input data provided"

        amenity = Amenity(name=data.get("name", ""), is_active=data.get("is_active", True))
        valid, error = amenity.validate()
        if not valid:
            return None, error

        self.amenity_repo.add(amenity)
        return amenity, None

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None, "Amenity not found"

        if not data:
            return None, "No input data provided"

        if "name" in data:
            amenity.name = (data.get("name") or "").strip()

        valid, error = amenity.validate()
        if not valid:
            return None, error

        return amenity, None

    # ================= PLACES =================
    def create_place(self, place_data):
        place = Place(**(place_data or {}))
        valid, error = place.validate()
        if not valid:
            return None, error

        if not self.get_user(place.owner_id):
            return None, "Owner not found"

        self.place_repo.add(place)
        return place, None

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, data):
        place = self.get_place(place_id)
        if not place:
            return None, "Place not found"

        if not data:
            return None, "No input data provided"

        for key, value in data.items():
            if hasattr(place, key):
                setattr(place, key, value)

        valid, error = place.validate()
        if not valid:
            return None, error

        if not self.get_user(place.owner_id):
            return None, "Owner not found"

        return place, None

    # ================= REVIEWS =================
    def create_review(self, data):
        if not data:
            return None, "No input data provided"

        review = Review(
            user_id=data.get("user_id"),
            place_id=data.get("place_id"),
            text=data.get("text"),
            rating=data.get("rating"),
        )

        valid, error = review.validate()
        if not valid:
            return None, error

        if not self.get_user(review.user_id):
            return None, "User not found"
        if not self.get_place(review.place_id):
            return None, "Place not found"

        self.review_repo.add(review)
        return review, None

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        if not self.get_place(place_id):
            return None, "Place not found"
        reviews = self.review_repo.get_all()
        return [r for r in reviews if getattr(r, "place_id", None) == place_id], None

    def update_review(self, review_id, data):
        review = self.get_review(review_id)
        if not review:
            return None, "Review not found"

        if not data:
            return None, "No input data provided"

        if "text" in data:
            review.text = data.get("text")
        if "rating" in data:
            review.rating = data.get("rating")

        valid, error = review.validate()
        if not valid:
            return None, error

        return review, None

    def delete_review(self, review_id):
        if not self.get_review(review_id):
            return False, "Review not found"
        self.review_repo.delete(review_id)
        return True, None

