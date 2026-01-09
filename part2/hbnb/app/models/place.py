from uuid import uuid4
from datetime import datetime


class Place:
    def __init__(
        self,
        owner_id: str,
        name: str,
        description: str = "",
        price_per_night: float = 0.0,
        latitude: float = None,
        longitude: float = None,
        amenity_ids: list[str] = None,
        place_id: str = None
    ):
        self.id = place_id or str(uuid4())
        self.owner_id = owner_id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids or []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def validate(self):
        if not self.name or not isinstance(self.name, str):
            return False, "Invalid name"

        if not isinstance(self.price_per_night, (int, float)) or self.price_per_night <= 0:
            return False, "Invalid price"

        if self.latitude is not None:
            if not isinstance(self.latitude, (int, float)) or not (-90 <= self.latitude <= 90):
                return False, "Invalid latitude"

        if self.longitude is not None:
            if not isinstance(self.longitude, (int, float)) or not (-180 <= self.longitude <= 180):
                return False, "Invalid longitude"

        if not self.owner_id or not isinstance(self.owner_id, str):
            return False, "Invalid owner_id"

        if not isinstance(self.amenity_ids, list):
            return False, "Invalid amenity_ids"

        return True, None

    def update(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "name": self.name,
            "description": self.description,
            "price_per_night": self.price_per_night,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "amenity_ids": self.amenity_ids,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
