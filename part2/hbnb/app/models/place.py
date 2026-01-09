# part2/hbnb/models/place.py
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

    def update(self, data: dict):
        # Update only allowed fields
        allowed = {
            "name", "description", "price_per_night",
            "latitude", "longitude", "amenity_ids"
        }
        for k, v in data.items():
            if k in allowed:
                setattr(self, k, v)
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
            "updated_at": self.updated_at.isoformat(),
        }
