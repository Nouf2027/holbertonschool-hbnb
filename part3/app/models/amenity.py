from app import db
from app.models.base_model import BaseModel
from app.models.place_amenity import place_amenity

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False, unique=True)

    places = db.relationship(
        'Place',
        secondary=place_amenity,
        back_populates='amenities'
    )
