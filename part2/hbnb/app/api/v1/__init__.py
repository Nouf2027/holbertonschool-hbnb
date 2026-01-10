from flask_restx import Api

from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns

api = Api(
    title="HBnB API",
    version="1.0",
    description="HBnB REST API"
)

api.add_namespace(places_ns, path="/api/v1/places")
api.add_namespace(reviews_ns, path="/api/v1/reviews")
