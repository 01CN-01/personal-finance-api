from pydantic import BaseModel

class RegisterCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    
    
    
    