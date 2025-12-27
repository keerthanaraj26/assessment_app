from fastapi import APIRouter, HTTPException, Request
import json

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
