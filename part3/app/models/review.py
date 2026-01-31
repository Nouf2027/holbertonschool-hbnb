#!/usr/bin/python3

from app import db
from app.models.base_model import BaseModel


class Review(BaseModel):
    __tablename__ = "reviews"

    text = db.Column(db.String(1024), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    place_id = db.Column(
        db.String(36),
        db.ForeignKey("places.id", ondelete="CASCADE"),
        nullable=False
    )

    user_id = db.Column(
        db.String(36),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    # Place (1) -> (*) Review
    place = db.relationship(
        "Place",
        back_populates="reviews"
    )

    # User (1) -> (*) Review
    author = db.relationship(
        "User",
        back_populates="reviews"
    )
