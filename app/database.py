# app/database.py

from pymongo import MongoClient
from dotenv import load_dotenv

import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URL from environment
MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["atlas_project_db"]

users_collection = db["users"]
products_collection = db["products"]

# uvicorn app.main:app --reload


# app/database.py

