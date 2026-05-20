from fastapi import FastAPI
from app.routers import loan

app = FastAPI(
    title="CarLoan Analyzer API",
    description="True cost of car ownership calculator",
    version="0.1.0"
)

app.include_router(loan.router, prefix = "/api/loan", tags = ["loan"])