from flask import Flask
from flask_jwt_extended import JWTManager
from .core.database import db
from .services.auth.routes import auth_bp

jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = "CodeRoyale"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://justinliu:@localhost:5432/coderoyale"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    jwt.init_app(app)
    db.init_app(app)

    app.register_blueprint(auth_bp)

    # Create tables
    from .services.users import models

    with app.app_context():
        db.create_all()
    
    return app
