from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, user_id, place_id, text, rating):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating

    def validate(self):
        if not self.text or not isinstance(self.text, str):
            return False, "Review text is required"

        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            return False, "Rating must be an integer between 1 and 5"

        if not self.user_id:
            return False, "User ID is required"

        if not self.place_id:
            return False, "Place ID is required"

        return True, None

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "user_id": self.user_id,
            "place_id": self.place_id,
            "text": self.text,
            "rating": self.rating
        })
        return data
