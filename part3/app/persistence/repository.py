from app import db
from app.persistence.repository import IRepository  

class SQLAlchemyRepository(IRepository):
    def __init__(self, model):
        """
This class, known as a 'model' (such as user, location), needs to know which table to interact with.
        """
        self.model = model

    def add(self, obj):
        """Adding a new element to the database """
        db.session.add(obj)
        db.session.commit()
        return obj

    def get(self, obj_id):
        """ "Retrieve an item by ID""""

        return db.session.get(self.model, obj_id)


    def get_all(self):
        """ Bring all the elements """
        return self.model.query.all()

    def get_by_attribute(self, attr_name, attr_value):
        """   Retrieve an item based on a specific condition (such as email) """
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()

    def update(self, obj_id, data):
        """ Update element data """
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            db.session.commit()
        return obj

    def delete(self, obj_id):
        """ delete item """
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
