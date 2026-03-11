from fastapi import FastAPI
from routers.auth import auth_router
from routers.finance import finance_router
from app.database import create_tables
app = FastAPI()

app.include_router(auth_router)
app.include_router(finance_router)

create_tables()