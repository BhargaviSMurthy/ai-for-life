import pytest
from fx.processor import FxRateProcessor
from fx.models import FxRate

@pytest.mark.asyncio
async def test_processor():
    class FakeClient:
        async def get_rate(self, date, currency):
            return 1.23  # constant value

    processor = FxRateProcessor(FakeClient())
    results = await processor.process_range(
        start_date, end_date, "EUR"
    )

    assert len(results) == 10
