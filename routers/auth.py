from fastapi import APIRouter
from uuid import uuid4    
from app.models.user import RegisterCreate
from app.security import hash_password
from app.database import create_account

auth_router = APIRouter(prefix = "/auth")

@auth_router.post("/register")
def register(register: RegisterCreate):
    print("PASSWORD VALUE:", register.password)
    print("PASSWORD LENGTH:", len(register.password))

    hashed_password = hash_password(register.password)
    
    user_UUID = str(uuid4())
    
    create_account(
                   user_UUID,
                   register.first_name,
                   register.last_name,
                   register.email,
                   hashed_password)
    
    return{"message": "User created"}