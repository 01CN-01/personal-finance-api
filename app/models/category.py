from pydantic import BaseModel

class CategoryCreate(BaseModel): # User gives us
    category: str

class CategoryResponse(BaseModel): # Database sends
    id: int
    category: str