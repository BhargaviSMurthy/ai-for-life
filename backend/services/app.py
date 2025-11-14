from fastapi import FastAPI
import asyncio
from datetime import datetime
from fx.api_client import FxApiClient
from fx.processor import FxRateProcessor

app = FastAPI()

@app.get("/fx")
async def get_fx(start: str, end: str, currency: str):
    start_dt = datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.strptime(end, "%Y-%m-%d")

    processor = FxRateProcessor(FxApiClient())
    return await processor.process_range(start_dt, end_dt, currency)
