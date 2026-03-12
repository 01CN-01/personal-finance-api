from fastapi import APIRouter
from app.models.category import CategoryCreate
from app.models.transaction import TransactionResponse
from app.database import make_category, get_transactions
finance_router = APIRouter(prefix = "/finance")

@finance_router.post("/create-category")
def create_category(category: CategoryCreate):
    make_category(category.name)
    return{"message": "Category created"}

# FInish
# @finance_router.get("/transactions", response_model = TransactionResponse)
# def get_transaction():
#     return get_transactions()