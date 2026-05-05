from flask import Blueprint, abort, jsonify
from flask_pydantic import validate
from flask_jwt_extended import create_access_token
from .dependencies import authenticate_user, get_user
from .schemas import Token
from app.services.users.models import User
from app.services.users.schemas import UserCreate, UserLogin, UserResponse
from .utils import get_password_hash
from app.core.database import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/token", methods=["POST"])
@validate()
def login_for_access_token(body: UserLogin) -> Token:
    user = authenticate_user(body.username, body.password)
    if not user:
        return jsonify({"message": "Incorrect username or password"}), 401
        # abort(401, description="Incorrect username or password")
    access_token = create_access_token(identity=body.username)
    return {"access_token": access_token, "token_type": "bearer"}

@auth_bp.route("/signup", methods=["POST"])
@validate()
def signup(body: UserCreate) -> UserResponse:
    # print(body)
    db_user = get_user(body.username)
    if db_user:
        return jsonify({"message": "Username is already registered"}), 400
        # abort(400, description="Username is already registered")
    # print(body)
    hashed_password = get_password_hash(body.password)
    db_user = User(username=body.username, hashed_password=hashed_password)
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)
    return UserResponse.model_validate(db_user)
