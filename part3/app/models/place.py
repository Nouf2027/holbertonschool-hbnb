from app import db
from app.models.base_model import BaseModel

class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)


    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    

