import aiohttp

BASE_URL = "https://www.deribit.com/api/v2/public/get_index_price"


class DeribitClient:

    async def get_index_price(self, ticker: str) -> float:

        params = {"index_name": ticker}

        async with aiohttp.ClientSession() as session:
            async with session.get(BASE_URL, params=params) as resp:
                data = await resp.json()
                return data["result"]["index_price"]