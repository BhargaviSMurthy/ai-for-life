import asyncio
from datetime import datetime
from fx.api_client import FxApiClient
from fx.processor import FxRateProcessor
from fx.storage import save_to_csv

async def main():
    start = datetime(2025, 1, 1)
    end = datetime(2025, 1, 10)

    processor = FxRateProcessor(FxApiClient())
    data = await processor.process_range(start, end, "EUR")

    save_to_csv("fx_output.csv", data)

if __name__ == "__main__":
    asyncio.run(main())
