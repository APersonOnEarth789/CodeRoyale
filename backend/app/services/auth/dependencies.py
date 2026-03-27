from flask import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import select
from .utils import verify_password
from app.services.users.models import User
from app.core.database import db

def get_user(username: str):
    return db.session.execute(select(User).filter_by(username=username)).scalar_one_or_none()

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

@jwt_required()
def get_current_user():
    username = get_jwt_identity()
    if not username:
        abort(401, description="Could not validate credentials")
    user = get_user(username)
    if not user:
        abort(401, description="Could not find user")
    return user
