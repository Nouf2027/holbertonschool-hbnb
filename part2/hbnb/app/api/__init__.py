from flask_restx import Api
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
api = Api(
    title="HBnB API",
    version="1.0",
    description="HBnB REST API"
)

api.add_namespace(amenities_ns, path="/api/v1/amenities")
api.add_namespace(places_ns, path="/api/v1/places")
