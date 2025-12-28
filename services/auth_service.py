from datetime import datetime
import uuid
from database import user_collection
from utils.security import hash_password, verify_password
from utils.jwt import create_access_token

async def authenticate_user(email: str, password: str):
    user = await user_collection.find_one({"email": email})

    if not user:
        return None

    if not verify_password(password, user["password_hash"]):
        return None

    token = create_access_token({
        "user_id": str(user["_id"]),
        "role": user["role"]
    })

    return {
        "access_token": token,
        "role": user["role"]
    }

async def create_user(user_data: dict):
    existing_user = await user_collection.find_one(
        {"email": user_data["email"]}
    )
    if existing_user:
        raise ValueError("User already exists")

    hashed_password = hash_password(user_data["password"])

    user_doc = {
        "_id": str(uuid.uuid4()),
        "name": user_data["name"],
        "email": user_data["email"],
        "password": hashed_password,
        "role": user_data["role"],
        "created_at": datetime.utcnow()
    }

    result = await user_collection.insert_one(user_doc)
    return result.inserted_id