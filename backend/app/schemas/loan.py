from pydantic import BaseModel, Field
from typing import List


class LoanRequest(BaseModel):
    principal: float = Field(..., gt=0, description="The amount of the loan")
    annual_rate: int = Field(..., gt=0,
                             description="The term of the loan in months")
    term_months: float = Field(..., gt=0,
                               description="The annual interest rate of the loan")


class AmortizationRow(BaseModel):
    month: int
    payment: float
    interest: float
    principal: float
    balance: float


class LoanResponse(BaseModel):
    monthly_payment: float
    total_paid: float
    total_interest: float
    schedule: List[AmortizationRow]
