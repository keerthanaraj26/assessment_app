from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    name: str
    email: EmailStr
    password_hash: str
    role: str   # admin / candidate
    is_active: bool = True
    created_at: datetime = datetime.utcnow()
