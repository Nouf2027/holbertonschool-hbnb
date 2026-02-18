from typing import Any, Dict


class SQLAlchemyRepository:
    def __init__(self, model):
        """Generic repository using SQLAlchemy models."""
        self.model = model

    def add(self, obj: Any):
        from app import db
        db.session.add(obj)
        db.session.commit()
        return obj

    def get(self, obj_id: str):
        from app import db
        return db.session.get(self.model, obj_id)

    def get_all(self):
        return self.model.query.all()

    def get_by_attribute(self, attr_name: str, attr_value):
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()

    def update(self, obj_id: str, data: Dict):
        obj = self.get(obj_id)
        if obj:
            for key, value in (data or {}).items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            from app import db
            db.session.commit()
        return obj

    def delete(self, obj_id: str):
        obj = self.get(obj_id)
        if obj:
            from app import db
            db.session.delete(obj)
            db.session.commit()


class InMemoryRepository:
    def __init__(self):
        self.store = {}

    def add(self, obj):
        self.store[getattr(obj, 'id')] = obj
        return obj

    def get(self, obj_id):
        return self.store.get(obj_id)

    def get_all(self):
        return list(self.store.values())

    def get_by_attribute(self, attr_name, attr_value):
        for obj in self.store.values():
            if getattr(obj, attr_name, None) == attr_value:
                return obj
        return None

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in (data or {}).items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
        return obj

    def delete(self, obj_id):
        return self.store.pop(obj_id, None)
