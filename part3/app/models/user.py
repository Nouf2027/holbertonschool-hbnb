from app.models.base_model import BaseModel
from app import bcrypt


class User(BaseModel):
    def __init__(self, **kwargs):
        super().__init__()

        self.first_name = kwargs.get("first_name", "").strip()
        self.last_name = kwargs.get("last_name", "").strip()
        self.email = kwargs.get("email", "").strip()

        
        self.password = None

        
        if "password" in kwargs:
            self.hash_password(kwargs.get("password"))

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        })

        return data

