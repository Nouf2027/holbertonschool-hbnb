from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()

    # ================= USERS =================
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        if not user:
            return None
        user.update(data)
        return user

    # ================= PLACES =================
    def create_place(self, place_data):
        place = Place(**place_data)
        valid, error = place.validate()
        if not valid:
            return None, error
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

        for key, value in data.items():
            if hasattr(place, key):
                setattr(place, key, value)

        valid, error = place.validate()
        if not valid:
            return None, error

        return place, None

    # ================= REVIEWS =================
    def create_review(self, data):
        if not data:
            return None, "No input data provided"

        if "text" not in data or not data["text"].strip():
            return None, "Text is required"

        if "rating" not in data:
            return None, "Rating is required"

        rating = data["rating"]
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return None, "Rating must be between 1 and 5"

        if "user_id" not in data:
            return None, "User ID is required"

        if "place_id" not in data:
            return None, "Place ID is required"

        review = Review(
            user_id=data["user_id"],
            place_id=data["place_id"],
            text=data["text"],
            rating=rating
        )

        self.review_repo.add(review)
        return review, None

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_all_by_attribute("place_id", place_id)
