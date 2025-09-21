from sqlalchemy import Column, Integer, String, Float, Boolean
from .db import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)   # <— back to id
    name = Column(String(120), nullable=False, index=True)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True, nullable=False)
    category = Column(String(60), default="general", nullable=False)
