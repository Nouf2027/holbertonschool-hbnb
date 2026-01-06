from app.models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, is_active=True):
        super().__init__()
        self.name = name
        self.is_active = is_active
