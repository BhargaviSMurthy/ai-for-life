from fastapi import APIRouter
from openai import OpenAI
from pydantic import BaseModel
from datetime import date
import os

from backend.utils.FinancialPlanInput import FinancialPlanInput
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
router = APIRouter()


@router.post("/financial-plan")
def create_financial_plan(financialPlanInput: FinancialPlanInput):
    
     # Prepare a context message for AI
    prompt = f"""
    You are a financial advisor. Based on the following client data:
    - Name: {financialPlanInput.first_name} {financialPlanInput.last_name}
    - Date of Birth: {financialPlanInput.dob}
    - Investment Type: {financialPlanInput.investment_type.value}
    - Risk Tolerance: {financialPlanInput.riskTolerance.value}
    - Family Income: {financialPlanInput.family_income}
    - Monthly Expenses: {financialPlanInput.monthly_expenses}
    - Maritial Status: {financialPlanInput.maritial_status.value}
    - Number of Dependents: {financialPlanInput.number_of_dependents}
    - Years to Invest: {financialPlanInput.years_to_invest}
    - Investment Amount: {financialPlanInput.investment_amount}
    - Investment Frequency: {financialPlanInput.investment_frequency.value}
    - Investment Goals: {financialPlanInput.investment_goals}
    - Investment Experience: {financialPlanInput.investment_experience.value}
    - Investment Horizon: {financialPlanInput.investment_horizon.value}
    - Target Return: {financialPlanInput.target_return}%
    Please  generate a comprehensive financial plan that includes as they totally relay on your expertise.:

    Provide:
    1. A clear recommended financial plan (short paragraph)
    2. 3 actionable investment suggestions
    3. A short note on expected risk/reward
    """

    # Call AI model
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-4-turbo, gpt-5, etc.
        messages=[
            {"role": "system", "content": "You are an expert financial planner."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    ai_plan = response.choices[0].message.content

    return {
        "name": f"{financialPlanInput.first_name} {financialPlanInput.last_name}",
        "date_of_birth": str(financialPlanInput.dob),
        "investment_type": financialPlanInput.investment_type,
        "ai_recommendation": ai_plan
    }