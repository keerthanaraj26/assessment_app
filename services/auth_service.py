from database import user_collection
from utils.security import verify_password
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
