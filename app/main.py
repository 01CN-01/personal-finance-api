from fastapi import FastAPI
from routers.auth import auth_router
from routers.finance import finance_router

app = FastAPI()

app.include_router(auth_router,finance_router)
