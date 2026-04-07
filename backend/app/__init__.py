from flask import Flask
from flask_jwt_extended import JWTManager
from .core.database import db
from .services.auth.routes import auth_bp
from .services.matchmaking.routes import matchmaking_bp

jwt = JWTManager()

def create_app(config_override=None):
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = "CodeRoyale"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://justinliu:@localhost:5432/coderoyale"
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
