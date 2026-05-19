from fastapi import FastAPI
from app.routers import loan

app = FastAPI()

app.include_router(loan.router, prefix = "/api/loan", tags = ["loan"])