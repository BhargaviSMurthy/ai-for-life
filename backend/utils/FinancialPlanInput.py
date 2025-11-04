from datetime import date
from groq import BaseModel
from matplotlib.pylab import Enum


class InvestmentType(str, Enum):
    growth = "growth"
    compounding = "compounding"
    medium = "medium"
    
class RiskTolerance(str, Enum):
    stock = "stock"
    mutual_funds = "mutual_funds"
    bonds = "bonds"
    etfs = "etfs"
    real_estate = "real_estate"
    commodities = "commodities"
    cryptocurrencies = "cryptocurrencies"
    savings_account = "savings_account"
    fixed_deposits = "fixed_deposits"
    retirement_accounts = "retirement_accounts"
    
class InvesestmentFrequency(str, Enum):
    monthly = "monthly"
    quarterly = "quarterly"
    yearly = "yearly"
    
class InvestmentExperience(str, Enum):
    none = "none"
    beginner = "beginner"
    intermediate = "intermediate"
    expert = "expert"
    
class InvestmentHorizon(str, Enum):
    short_term = "short-term"
    medium_term = "medium-term"
    long_term = "long-term"
    
class MaritialStatus(str, Enum):
    single = "single"
    married = "married"
    divorced = "divorced"
    widowed = "widowed"

class FinancialPlanInput(BaseModel):
    first_name: str # user's first name
    last_name: str # user's last name
    dob: date # date of birth (YYYY-MM-DD)
    riskTolerance: RiskTolerance  # growth, compounding, or medium
    investment_type: InvestmentType  # stock, mutual funds, bonds, etc.
    family_income: float # annual family income
    monthly_expenses: float # average monthly expenses
    maritial_status: MaritialStatus  # single, married, etc.
    family_income: float # annual family income
    number_of_dependents: int  # number of dependents
    years_to_invest: int # number of years to invest
    investment_amount: float # amount to invest
    investment_frequency: InvesestmentFrequency  # monthly, quarterly, yearly
    investment_goals: str  # retirement, wealth accumulation, education, etc.
    investment_experience: InvestmentExperience  # none, beginner, intermediate, expert
    investment_horizon: InvestmentHorizon  # short-term, medium-term, long-term
    target_return: float  # expected annual return percentage
    
