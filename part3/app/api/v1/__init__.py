from flask_restx import Api

from app.api.v1.users import api as users_api
from app.api.v1.auth import api as auth_api
from app.api.v1.protected import api as protected_api


def init_api(app):
    api = Api(app, version="1.0", title="HBnB API", description="HBnB API")

    api.add_namespace(users_api, path="/api/v1/users")
    api.add_namespace(auth_api, path="/api/v1/auth")
    api.add_namespace(protected_api, path="/api/v1")

    return api
