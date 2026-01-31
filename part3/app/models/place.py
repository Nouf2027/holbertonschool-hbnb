from app import db
from app.models.base_model import BaseModel
from app.models.place_amenity import place_amenity

class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    owner_id = db.Column(
        db.String(36),
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )

    # User (1) -> (*) Place
    owner = db.relationship(
        'User',
        back_populates='places'
    )

    # Place (1) -> (*) Review
    reviews = db.relationship(
        'Review',
        back_populates='place',
        cascade='all, delete-orphan',
        passive_deletes=True
    )

    # Place (*) <-> (*) Amenity
    amenities = db.relationship(
        'Amenity',
        secondary=place_amenity,
        back_populates='places'
    )
