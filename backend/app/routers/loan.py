from fastapi import APIRouter
from app.services.loan import calculate_amortization
from app.schemas.loan import LoanRequest, LoanResponse

router = APIRouter()


@router.post("/amortize", response_model=LoanResponse)
def amortize_loan(loan_request: LoanRequest):
    result = calculate_amortization(loan_request.principal, loan_request.annual_rate, loan_request.term_months)
    return result

