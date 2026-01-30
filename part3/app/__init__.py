from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.api.v1 import init_api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bcrypt.init_app(app)
    jwt.init_app(app)

    init_api(app)

    return app
