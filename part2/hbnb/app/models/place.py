from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, owner_id, price_per_night, latitude, longitude, description=""):
        super().__init__()
        self.name = name
        self.owner_id = owner_id
        self.description = description
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.reviews = []
        self.amenities = []
