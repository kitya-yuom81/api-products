# app/deps.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from .config import settings
from .db import get_db  # keep if other deps use it
from .security import DEMO_USER, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if username != DEMO_USER["username"]:
            raise HTTPException(status_code=401, detail="Invalid token subject")
        return {"username": username, "full_name": DEMO_USER["full_name"]}
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
