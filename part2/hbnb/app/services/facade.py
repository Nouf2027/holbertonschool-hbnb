from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.users = InMemoryRepository()
        self.places = InMemoryRepository()
        self.reviews = InMemoryRepository()
        self.amenities = InMemoryRepository()

    def create_user(self, data):
        pass

    def get_place(self, place_id):
        pass
