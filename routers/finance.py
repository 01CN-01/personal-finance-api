from fastapi import APIRouter, HTTPException
from uuid import uuid4
from app.models.category import CategoryCreate
from app.models.transaction import TransactionResponse, TransactionCreate
from app.database import make_category, get_transactions, get_categories, create_transactions, delete_transaction
finance_router = APIRouter(prefix = "/finance")

@finance_router.post("/create-category")
def create_category(category: CategoryCreate):
    created = make_category(category.category)
    
    if created:
        return {"message": "Successfully created category"}
    else:
        return {"message": "Category already exists"}    

@finance_router.get("/categories")
def categories():
    all_categories = get_categories()
    return all_categories

@finance_router.post("/create-transaction/{user_UUID}")
def create_transaction(transaction: TransactionCreate):
    UUID = str(uuid4())
    create_transactions(UUID,
                        transaction.user_UUID,
                        transaction.category_id,
                        transaction.description,
                        transaction.amount)
    
@finance_router.get("/transactions/{user_UUID}", response_model=list[TransactionResponse])
def get_transaction(user_UUID: str):
    transactions = get_transactions(user_UUID)
    if transactions:
        return transactions
    else:
        raise HTTPException(status_code=404, detail="No transactions found")

@finance_router.delete("/delete-transaction/{UUID}")
def delete_transactions(UUID: str, user_UUID: str):
    deleted = delete_transaction(UUID, user_UUID)
    
    if deleted:
        return {"message": "Transaction deleted successfully"}
    else:
       return {"message": "Transaction not found"}
