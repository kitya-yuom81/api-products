from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    price: float = Field(..., ge=0)
    in_stock: bool = True
    category: str = Field("general", min_length=1, max_length=60)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=120)
    price: Optional[float] = Field(None, ge=0)
    in_stock: Optional[bool] = None
    category: Optional[str] = Field(None, min_length=1, max_length=60)

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginInput(BaseModel):
    username: str
    password: str
