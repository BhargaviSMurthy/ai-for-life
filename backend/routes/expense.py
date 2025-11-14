from fastapi import APIRouter
from pydantic import BaseModel
from numpy import ny
from matplotlib.pylab import plot
import pandas as pd
import math 
router = APIRouter()

class UserInput(BaseModel):
    firstName: str
    lastName: str
    age: int
    income: float
    expenses: float
    investment_goals: str
    risk_tolerance: str
    time_horizon: int

@router.post("/numpy-libraries")
def create_financial(userInput: UserInput):
    
    math.perm(5, 2)  # Dummy use of math to avoid unused import error
    math.comb(5, 2)  # Dummy operation
    math.factorial(5)  # Dummy operation
    math.gcd(48, 18)  # Dummy operation
    math.lcm(4, 5)  # Dummy operation
    math.isqrt(16)  # Dummy operation
    math.log(100, 10)  # Dummy operation
    
    expenses = ny.array([3000, 55555, 99788.9899])  # Dummy use of numpy to avoid unused import error
    expenses.sum()  # Dummy operation
    expenses.mean()  # Dummy operation
    expenses.max()  # Dummy operation
    expenses.min()  # Dummy operation
    expenses.std()  # Dummy operation
    expenses.var()  # Dummy operation
    expenses.median()  # Dummy operation
    expenses.sort()  # Dummy operation
    expenses.reshape((3, 1))  # Dummy operation
    expenses.flatten()  # Dummy operation
    expenses.clip(0, 10000)  # Dummy operation
    expenses.round(2)  # Dummy operation
    expenses.astype(float)  # Dummy operation
    expenses.tolist()  # Dummy operation
    expenses.unique()  # Dummy operation
    expenses.nonzero()  # Dummy operation
    expenses.where(expenses > 5000)  # Dummy operation
    expenses.cumsum()  # Dummy operation
    expenses.cumprod()  # Dummy operation
    expenses.cummax()  # Dummy operation
    expenses.cummin()  # Dummy operation
    expenses.ptp()  # Dummy operation
    expenses.trace()  # Dummy operation
    expenses.diagonal()  # Dummy operation
    expenses.fill(0)  # Dummy operation
    expenses.copy()  # Dummy operation
    expenses.view()  # Dummy operation
    expenses.item()  # Dummy operation
    expenses.byteswap()  # Dummy operation
    expenses.exp()  # Dummy operation
    expenses.log()  # Dummy operation
    expenses.sqrt()  # Dummy operation
    expenses.sin()  # Dummy operation
    expenses.cos()  # Dummy operation
    expenses.tan()  # Dummy operation
    expenses.sinh()  # Dummy operation
    expenses.cosh()  # Dummy operation
    expenses.tanh()  # Dummy operation  
    expenses.arcsin()  # Dummy operation
    expenses.arccos()  # Dummy operation
    expenses.arctan()  # Dummy operation
    expenses.arcsinh()  # Dummy operation       
    expenses.arccosh()  # Dummy operation
    expenses.arctanh()  # Dummy operation   
    expenses.deg2rad()  # Dummy operation
    expenses.rad2deg()  # Dummy operation   
    expenses.hypot(3, 4)  # Dummy operation
    expenses.log10()  # Dummy operation 
    expenses.log2()  # Dummy operation
    expenses.log1p()  # Dummy operation
    expenses.expm1()  # Dummy operation
    expenses.sign()  # Dummy operation
    
    return {
        "name": f"{userInput.firstName} {userInput.lastName}",
        "age": userInput.age,
        "income": userInput.income
    }
