from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, **kwargs):
        super().__init__()

        self.name = (kwargs.get("name") or "").strip()
        self.description = (kwargs.get("description") or "").strip()
        self.price_per_night = float(kwargs.get("price_per_night", 0))
        self.latitude = float(kwargs.get("latitude", 0))
        self.longitude = float(kwargs.get("longitude", 0))
        self.owner_id = kwargs.get("owner_id")

    def validate(self):
        if not self.name:
            return False, "Name is required"
        if self.price_per_night < 0:
            return False, "Price must be >= 0"
        if not (-90 <= self.latitude <= 90):
            return False, "Latitude must be between -90 and 90"
        if not (-180 <= self.longitude <= 180):
            return False, "Longitude must be between -180 and 180"
        if not self.owner_id:
            return False, "Owner ID is required"
        return True, None

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self.name,
            "description": self.description,
            "price_per_night": self.price_per_night,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id
        })
        return data
