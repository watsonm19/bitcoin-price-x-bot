import httpx


async def fetch_bitcoin_price(api_key: str, currency: str = "USD") -> float:
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {
        "X-CMC_PRO_API_KEY": api_key,
    }
    params = {
        "symbol": "BTC",
        "convert": currency
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        data = response.json()

        if response.is_error:
            raise Exception(f"Error fetching data from CoinMarketCap: {data['status']['error_message']}")

        price = data["data"]["BTC"]["quote"][currency]["price"]
        return price
