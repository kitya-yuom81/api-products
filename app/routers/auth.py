from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import Token
from ..config import settings
from ..security import DEMO_USER, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != DEMO_USER["username"] or not verify_password(form_data.password, DEMO_USER["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    token = create_access_token(
        data={"sub": DEMO_USER["username"]},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": token, "token_type": "bearer"}
