from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date

router = APIRouter()

class UserInput(BaseModel):
    first_name: str
    last_name: str
    dob: date
    investment_type: str  # growth, compounding, or medium

@router.post("/financial-plan")
def create_financial_plan(data: UserInput):
    # Simple logic based on investment type
    plans = {
        "growth": "Aggressive portfolio with high-risk equity funds",
        "compounding": "Balanced mix of reinvested mutual funds and recurring deposits",
        "medium": "Moderate-risk portfolio with stable debt funds"
    }

    plan_description = plans.get(data.investment_type.lower(), "Custom plan based on advisor consultation")

    return {
        "name": f"{data.first_name} {data.last_name}",
        "date_of_birth": str(data.dob),
        "investment_type": data.investment_type,
        "financial_plan": plan_description
    }
