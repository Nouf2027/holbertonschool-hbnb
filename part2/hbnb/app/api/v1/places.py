from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = (kwargs.get("title") or "").strip()
        self.description = (kwargs.get("description") or "").strip()
        self.price = float(kwargs.get("price", 0))
        self.latitude = float(kwargs.get("latitude", 0))
        self.longitude = float(kwargs.get("longitude", 0))
        self.owner_id = (kwargs.get("owner_id") or "").strip()
        self.amenity_ids = list(kwargs.get("amenity_ids", []))

    def validate(self):
        if not self.title:
            return False, "Title is required"
        if not isinstance(self.title, str):
            return False, "Title must be a string"
        if len(self.title) > 100:
            return False, "Title too long"

        if not isinstance(self.price, (int, float)) or self.price <= 0:
            return False, "Invalid price"

        if not (-90 <= self.latitude <= 90):
            return False, "Invalid latitude"

        if not (-180 <= self.longitude <= 180):
            return False, "Invalid longitude"

        if not self.owner_id:
            return False, "Owner ID is required"

        if not isinstance(self.amenity_ids, list):
            return False, "Amenity IDs must be a list"

        return True, None

    def add_amenity(self, amenity_id):
        if amenity_id not in self.amenity_ids:
            self.amenity_ids.append(amenity_id)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenity_ids": self.amenity_ids
        })
        return data
