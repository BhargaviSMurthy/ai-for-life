import aiohttp
from .exceptions import FxError
from .logger import logger

class FxApiClient:

    BASE_URL = "https://api.exchangerate.host/"

    async def get_rate(self, date, currency):
        url = f"{self.BASE_URL}{date}?base=USD&symbols={currency}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status != 200:
                        raise FxError(f"API returned {resp.status}")

                    data = await resp.json()
                    return data["rates"][currency]

        except Exception:
            logger.exception("Failed to fetch FX rate")
            raise
