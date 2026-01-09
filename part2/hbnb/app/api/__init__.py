from flask_restx import Api
from app.api.v1.amenities import api as amenities_ns

api = Api(
    title="HBnB API",
    version="1.0",
    description="HBnB REST API"
)

api.add_namespace(amenities_ns, path="/api/v1/amenities")
