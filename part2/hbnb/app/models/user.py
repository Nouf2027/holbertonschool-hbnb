from app.models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, **kwargs):
        super().__init__()

        self.first_name = kwargs.get("first_name", "").strip()
        self.last_name = kwargs.get("last_name", "").strip()
        self.email = kwargs.get("email", "").strip()

    def validate(self):
        if not self.first_name:
            return False, "First name is required"
        if not self.last_name:
            return False, "Last name is required"
        if not self.email:
            return False, "Email is required"
        if "@" not in self.email or "." not in self.email:
            return False, "Invalid email format"
        return True, None

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        })
        return data
