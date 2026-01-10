from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


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

        user = User(**user_data)
        valid, error = user.validate()
        if not valid:
            return None, error

        existing = self.get_user_by_email(user.email)
        if existing:
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

        for key, value in (data or {}).items():
            if hasattr(user, key):
                setattr(user, key, (value.strip() if isinstance(value, str) else value))

        valid, error = user.validate()
        if not valid:
            return None, error

        other = self.get_user_by_email(user.email)
        if other and other.id != user.id:
            return None, "Email already exists"

        return user, None

    # ================= AMENITIES =================
    def create_amenity(self, amenity_data):
        if not amenity_data:
            return None, "No input data provided"

        amenity = Amenity(**amenity_data)
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

        for key, value in (data or {}).items():
            if hasattr(amenity, key):
                setattr(amenity, key, (value.strip() if isinstance(value, str) else value))

        valid, error = amenity.validate()
        if not valid:
            return None, error

        return amenity, None

    # ================= PLACES =================
    def create_place(self, place_data):
        if not place_data:
            return None, "No input data provided"

        place = Place(**place_data)
        valid, error = place.validate()
        if not valid:
            return None, error

        owner = self.get_user(place.owner_id)
        if not owner:
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

        for key, value in (data or {}).items():
            if hasattr(place, key):
                setattr(place, key, value)

        valid, error = place.validate()
        if not valid:
            return None, error

        owner = self.get_user(place.owner_id)
        if not owner:
            return None, "Owner not found"

        return place, None

    # ================= REVIEWS =================
    def create_review(self, data):
        if not data:
            return None, "No input data provided"

        text = data.get("text")
        rating = data.get("rating")
        user_id = data.get("user_id")
        place_id = data.get("place_id")

        if text is None or not isinstance(text, str) or not text.strip():
            return None, "Text is required"

        if rating is None:
            return None, "Rating is required"
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return None, "Rating must be between 1 and 5"

        if not user_id or not isinstance(user_id, str):
            return None, "User ID is required"

        if not place_id or not isinstance(place_id, str):
            return None, "Place ID is required"

        user = self.get_user(user_id)
        if not user:
            return None, "User not found"

        place = self.get_place(place_id)
        if not place:
            return None, "Place not found"

        review = Review(
            user_id=user_id,
            place_id=place_id,
            text=text.strip(),
            rating=rating
        )

        valid, error = review.validate()
        if not valid:
            return None, error

        self.review_repo.add(review)
        return review, None

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.get_place(place_id)
        if not place:
            return None, "Place not found"

        reviews = [r for r in self.review_repo.get_all() if getattr(r, "place_id", None) == place_id]
        return reviews, None

    def update_review(self, review_id, data):
        review = self.get_review(review_id)
        if not review:
            return None, "Review not found"

        if not data:
            return None, "No input data provided"

        if "text" in data:
            text = data.get("text")
            if text is None or not isinstance(text, str) or not text.strip():
                return None, "Text is required"
            review.text = text.strip()

        if "rating" in data:
            rating = data.get("rating")
            if not isinstance(rating, int) or rating < 1 or rating > 5:
                return None, "Rating must be between 1 and 5"
            review.rating = rating

        valid, error = review.validate()
        if not valid:
            return None, error

        return review, None

    def delete_review(self, review_id):
        review = self.get_review(review_id)
        if not review:
            return False, "Review not found"

        self.review_repo.delete(review_id)
        return True, None

