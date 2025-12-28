from fastapi import APIRouter, HTTPException, Request
import json

from models.user_model import UserCreate
from services.auth_service import create_user

router = APIRouter(prefix="/api/auth")

@router.post("/login")
async def login(request: Request):
    try:
        body = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Invalid or empty JSON body"
        )

    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        raise HTTPException(
            status_code=400,
            detail="email and password are required"
        )

    # authentication logic here
    return {"message": "Login payload received"}

@router.post("/register")
async def register(user: UserCreate):
    try:
        user_id = await create_user(user.dict())
        return {
            "message": "User registered successfully",
            "user_id": user_id
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))