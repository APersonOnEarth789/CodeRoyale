from flask import Flask
from flask_jwt_extended import JWTManager
from .core.database import db
from .services.auth.routes import auth_bp
from .services.matchmaking.routes import matchmaking_bp
import os

jwt = JWTManager()

def create_app(config_override=None):
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = "CodeRoyaleSuperSecureKey1234567890!"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if config_override:
        app.config.update(config_override)

    jwt.init_app(app)
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(matchmaking_bp)

    # Register tables
    from .services.users import models
    
    return app
