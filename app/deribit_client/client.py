import requests

BASE_URL = "https://www.deribit.com/api/v2/public/get_index_price"


class DeribitClient:
    def get_index_price(self, ticker: str) -> float:
        params = {"index_name": ticker}
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        return data["result"]["index_price"]
