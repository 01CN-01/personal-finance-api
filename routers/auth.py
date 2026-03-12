from fastapi import APIRouter, HTTPException
from uuid import uuid4    
from app.models.user import RegisterCreate, LoginCreate, LoginResponse
from app.security import hash_password, verify_password
from app.database import create_account, get_user_by_email

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

@auth_router.post("/login", response_model = LoginResponse)
def login(login: LoginCreate):
    user = get_user_by_email(login.email)
    
    if not user: # Couldn't find email
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    if not verify_password(login.password, user["encrypted_password"]):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    return {
        "user_UUID": user["UUID"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"]
    }
    
    