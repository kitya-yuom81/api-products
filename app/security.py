from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext  # 🔥 move this up
from .config import settings

ALGORITHM = "HS256"

DEMO_USER = {
    "username": "admin",
    "full_name": "Admin User",
    "hashed_password": "$2b$12$Y.QxvM9W1sA5kC2H0k3r8OSv1yfdvQqXxq8x3C1L8m3y8g1m6q0r2"  # bcrypt for 'admin123'
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
