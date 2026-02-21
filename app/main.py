# app/main.py

from fastapi import FastAPI, HTTPException
from app.database import users_collection, products_collection
from app.schemas import (
    UserCreate, UserResponse,
    ProductCreate, ProductResponse
)

app = FastAPI()


# ========================
# USER ENDPOINTS
# ========================

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):

    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    users_collection.insert_one(user.dict())

    return user


@app.get("/users/{email}", response_model=UserResponse)
def get_user(email: str):

    user = users_collection.find_one({"email": email})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(**user)


# ========================
# PRODUCT ENDPOINTS
# ========================

@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate):

    existing_product = products_collection.find_one({"sku": product.sku})

    if existing_product:
        raise HTTPException(status_code=400, detail="SKU already exists")

    products_collection.insert_one(product.dict())

    return product


@app.get("/products/{sku}", response_model=ProductResponse)
def get_product(sku: str):

    product = products_collection.find_one({"sku": sku})

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return ProductResponse(**product)