# app/schemas.py

from pydantic import BaseModel
from typing import Optional


# -------- USER --------

class UserCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None


class UserResponse(UserCreate):
    pass


# -------- PRODUCT --------

class ProductCreate(BaseModel):
    sku: str
    name: str
    price: float
    stock: int
    description: Optional[str] = None


class ProductResponse(ProductCreate):
    pass