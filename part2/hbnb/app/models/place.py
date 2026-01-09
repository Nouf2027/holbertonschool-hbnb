from app.models.base_model import BaseModel


class Place(BaseModel):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = (kwargs.get("name") or "").strip()
        self.description = (kwargs.get("description") or "").strip()
        self.price_per_night = float(kwargs.get("price_per_night", 0))
        self.latitude = float(kwargs.get("latitude", 0))
        self.longitude = float(kwargs.get("longitude", 0))
        self.owner_id = (kwargs.get("owner_id") or "").strip()
        self.amenity_ids = list(kwargs.get("amenity_ids", []))

    def validate(self):
        if not self.name:
            return False, "Name is required"
        if not isinstance(self.name, str):
            return False, "Name must be a string"
        if len(self.name) > 100:
            return False, "Name must be under 100 characters"

        if not isinstance(self.price_per_night, (int, float)):
            return False, "Price must be a number"
        if self.price_per_night <= 0:
            return False, "Price must be greater than 0"

        if not isinstance(self.latitude, (int, float)):
            return False, "Latitude must be a number"
        if not (-90 <= self.latitude <= 90):
            return False, "Latitude must be between -90 and 90"

        if not isinstance(self.longitude, (int, float)):
            return False, "Longitude must be a number"
        if not (-180 <= self.longitude <= 180):
            return False, "Longitude must be between -180 and 180"

        if not self.owner_id:
            return False, "Owner ID is required"
        if not isinstance(self.owner_id, str):
            return False, "Owner ID must be a string"

        if self.description and len(self.description) > 1000:
            return False, "Description must be under 1000 characters"

        if not isinstance(self.amenity_ids, list):
            return False, "Amenity IDs must be a list"

        return True, None

    def add_amenity(self, amenity_id: str):
        if amenity_id and amenity_id not in self.amenity_ids:
            self.amenity_ids.append(amenity_id)

    def remove_amenity(self, amenity_id: str):
        if amenity_id in self.amenity_ids:
            self.amenity_ids.remove(amenity_id)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self.name,
            "description": self.description,
            "price_per_night": self.price_per_night,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenity_ids": self.amenity_ids
        })
        return data
