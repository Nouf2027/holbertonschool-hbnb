from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.users import api as users_ns  # ✅ أضفنا users


def create_app():
    app = Flask(__name__)

    CORS(app)

    api = Api(
        app,
        title="HBnB API",
        version="1.0",
        description="HBnB REST API"
    )

     namespaces
    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(amenities_ns, path="/api/v1/amenities")
    api.add_namespace(places_ns, path="/api/v1/places")

    return app
