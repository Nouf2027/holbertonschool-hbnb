#!/usr/bin/python3

import re
from app.models.base_model import BaseModel
from app import db, bcrypt

from sqlalchemy.orm import validates


class User(BaseModel):
    __tablename__ = 'users'

    # --- Columns ---
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=False)

    password_hash = db.Column(db.String(128), nullable=False)

    # --- Relationships ---
    places = db.relationship(
        "Place",
        back_populates="owner",
        lazy="select",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    reviews = db.relationship(
        "Review",
        back_populates="author",
        lazy="select",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    # --- Password Logic  ---
    @property
    def password(self):
        """Prevents access to raw password"""
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        """Hashes password automatically when user.password = '...' is called"""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Checks if password matches the hash"""
        return bcrypt.check_password_hash(self.password_hash, password)

    # --- Validators ---
    @validates('first_name')
    def validate_first_name(self, key, value):
        if not value or not isinstance(value, str):
            raise ValueError("first_name must be a non-empty string")
        if len(value) > 50:
            raise ValueError("first_name must be at most 50 characters")
        return value

    @validates('last_name')
    def validate_last_name(self, key, value):
        if not value or not isinstance(value, str):
            raise ValueError("last_name must be a non-empty string")
        if len(value) > 50:
            raise ValueError("last_name must be at most 50 characters")
        return value

    @validates('email')
    def validate_email(self, key, value):
        if not value or not isinstance(value, str):
            raise ValueError("email must be a non-empty string")

        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.match(email_pattern, value):
            raise ValueError("email must be a valid email address")

        return value.lower()
