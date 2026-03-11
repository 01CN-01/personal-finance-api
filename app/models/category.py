from pydantic import BaseModel

class CategoryCreate(BaseModel): # User gives us
    name: str

class CategoryResponse(BaseModel): # Database sends
    id: int
    name: str