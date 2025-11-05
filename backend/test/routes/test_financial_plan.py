import unittest
from types import SimpleNamespace
import datetime

# Import the function under test
from backend.routes import financial_plan

# Try to import the FinancialPlanInput model; if it's not available, create a minimal stand-in
try:
    from backend.utils.FinancialPlanInput import FinancialPlanInput
except Exception:
    from pydantic import BaseModel
    from enum import Enum

    class DummyEnum(Enum):
        LOW = "low"
        MEDIUM = "medium"
        HIGH = "high"

    class FinancialPlanInput(BaseModel):
        first_name: str = "Test"
        last_name: str = "User"
        dob: datetime.date = datetime.date(1990, 1, 1)
        investment_type: DummyEnum = DummyEnum.MEDIUM
        riskTolerance: DummyEnum = DummyEnum.MEDIUM
        family_income: int = 50000
        monthly_expenses: int = 2000
        maritial_status: DummyEnum = DummyEnum.MEDIUM
        number_of_dependents: int = 0
        years_to_invest: int = 10
        investment_amount: int = 10000
        investment_frequency: DummyEnum = DummyEnum.MEDIUM
        investment_goals: str = "retirement"
        investment_experience: DummyEnum = DummyEnum.LOW
        investment_horizon: DummyEnum = DummyEnum.MEDIUM
        target_return: float = 5.0


class DummyResponse:
    def __init__(self, content: str):
        # Mirror the structure used in the route: response.choices[0].message.content
        self.choices = [SimpleNamespace(message=SimpleNamespace(content=content))]


class FinancialPlanTestCase(unittest.TestCase):
    def setUp(self):
        # Backup real client and replace with a dummy
        self._real_client = getattr(financial_plan, 'client', None)

        class DummyClient:
            class chat:
                class completions:
                    @staticmethod
                    def create(*args, **kwargs):
                        return DummyResponse("Recommended plan: Diversify and hold.")

        financial_plan.client = DummyClient()

    def tearDown(self):
        # Restore original client
        financial_plan.client = self._real_client

    def test_create_financial_plan_returns_ai_recommendation(self):
        sample = FinancialPlanInput(
            first_name="Alice",
            last_name="Example",
            dob=datetime.date(1985, 5, 5),
            investment_type=getattr(FinancialPlanInput.__annotations__.get('investment_type'), 'LOW', None) or getattr(FinancialPlanInput, 'investment_type', None) or getattr(FinancialPlanInput, 'investment_type', None),
            riskTolerance=getattr(FinancialPlanInput.__annotations__.get('riskTolerance'), 'LOW', None) or getattr(FinancialPlanInput, 'riskTolerance', None) or getattr(FinancialPlanInput, 'riskTolerance', None),
            family_income=75000,
            monthly_expenses=2500,
            maritial_status=getattr(FinancialPlanInput.__annotations__.get('maritial_status'), 'MEDIUM', None) or getattr(FinancialPlanInput, 'maritial_status', None) or getattr(FinancialPlanInput, 'maritial_status', None),
            number_of_dependents=2,
            years_to_invest=20,
            investment_amount=20000,
            investment_frequency=getattr(FinancialPlanInput.__annotations__.get('investment_frequency'), 'MEDIUM', None) or getattr(FinancialPlanInput, 'investment_frequency', None) or getattr(FinancialPlanInput, 'investment_frequency', None),
            investment_goals="College and retirement",
            investment_experience=getattr(FinancialPlanInput.__annotations__.get('investment_experience'), 'LOW', None) or getattr(FinancialPlanInput, 'investment_experience', None) or getattr(FinancialPlanInput, 'investment_experience', None),
            investment_horizon=getattr(FinancialPlanInput.__annotations__.get('investment_horizon'), 'MEDIUM', None) or getattr(FinancialPlanInput, 'investment_horizon', None) or getattr(FinancialPlanInput, 'investment_horizon', None),
            target_return=6.5,
        )

        result = financial_plan.create_financial_plan(sample)
        self.assertIn('ai_recommendation', result)
        self.assertIsInstance(result['ai_recommendation'], str)
        self.assertTrue(result['ai_recommendation'].startswith("Recommended plan:"))


if __name__ == '__main__':
    unittest.main()
