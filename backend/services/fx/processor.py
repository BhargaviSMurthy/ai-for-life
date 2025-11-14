from datetime import timedelta
from .models import FxRate
from .holidays import is_holiday

class FxRateProcessor:

    def __init__(self, api_client):
        self.api = api_client

    async def process_range(self, start, end, currency):
        results = []
        prev_rate = None

        current = start

        while current <= end:
            date_str = current.strftime("%Y-%m-%d")
            holiday = is_holiday(current)

            if not holiday:
                rate = await self.api.get_rate(date_str, currency)
                prev_rate = rate
                results.append(FxRate(date_str, currency, rate, False, 1))
            else:
                results.append(FxRate(date_str, currency, prev_rate, True, 2))

            current += timedelta(days=1)

        return results
