from flask import g, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import select
from sqlalchemy.orm import scoped_session
from .utils import verify_password
from app.services.users.models import User
from app.core.database import SessionLocal

def get_db():
    if "db" not in g:
        g.db = scoped_session(SessionLocal)
    return g.db

def get_user(username: str):
    return get_db().execute(select(User).filter_by(username=username)).scalar_one_or_none()

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
