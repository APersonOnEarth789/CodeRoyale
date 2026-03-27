from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "CodeRoyale"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(plain_password: str):
    return pwd_context.hash(plain_password)
