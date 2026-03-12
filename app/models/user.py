from pydantic import BaseModel, EmailStr

class RegisterCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    
class LoginCreate(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    user_UUID: str
    first_name: str
    last_name: str
    email: EmailStr
    
    
    
    