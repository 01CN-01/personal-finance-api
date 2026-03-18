from pydantic import BaseModel

class TransactionCreate(BaseModel):
    user_UUID: str
    category_id: int
    description: str
    amount: float

class TransactionResponse(BaseModel):
    transaction_UUID: str
    user_UUID: str
    category_id: int
    description: str
    amount: float
    created_at: str 
    
    

