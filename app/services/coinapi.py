import httpx
import datetime


async def fetch_bitcoin_price_at_year_start(api_key: str, currency: str = "USD") -> float:
    # Calculate the start of the current year
    year_start = datetime.datetime.now().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    start_date = year_start.strftime('%Y-%m-%dT%H:%M:%S')
    end_date = (year_start + datetime.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')

    # CoinAPI requires symbols in a specific format, e.g., "BITSTAMP_SPOT_BTC_USD"
    # You'll need to adjust the symbol_id according to CoinAPI's format and the specific market you're interested in
    symbol_id = f"BITSTAMP_SPOT_BTC_{currency}"

    url = f"https://rest.coinapi.io/v1/ohlcv/{symbol_id}/history"
    headers = {
        "X-CoinAPI-Key": api_key,
    }
    params = {
        "period_id": "1DAY",  # Assuming daily data is what you're after
        "time_start": start_date,
        "time_end": end_date,
        "limit": 1  # We only need the first available price at the start of the year
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        data = response.json()

        if response.status_code != 200:
            # Adjust error handling based on CoinAPI's error response structure
            error_message = data.get('error', 'Unknown error fetching historical data from CoinAPI')
            raise Exception(f"Error fetching historical data from CoinAPI: {error_message}")

        # Assuming the response contains an array of OHLCV data
        if data:
            # You might want to adjust which part of the OHLCV data you consider the "price"
            # For example, using the opening price
            price_at_start = data[0]["price_open"]
            return price_at_start
        else:
            raise Exception("No historical price data found for the specified date")


async def fetch_bitcoin_price_4_years_ago(api_key: str, currency: str = "USD") -> float:
    # Calculate the date 4 years ago from the current date
    four_years_ago_start = datetime.datetime.now() - datetime.timedelta(days=4*365)
    # Adjust for leap years (simplified, consider more precise adjustments for production use)
    four_years_ago_start = four_years_ago_start.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    start_date = four_years_ago_start.strftime('%Y-%m-%dT%H:%M:%S')
    # Assuming we want the price for the entire day, the end date is the next day
    end_date = (four_years_ago_start + datetime.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')

    # Adjust the symbol_id as needed for your specific data source and currency
    symbol_id = f"BITSTAMP_SPOT_BTC_{currency}"

    url = f"https://rest.coinapi.io/v1/ohlcv/{symbol_id}/history"
    headers = {
        "X-CoinAPI-Key": api_key,
    }
    params = {
        "period_id": "1DAY",  # Daily data is what we're after
        "time_start": start_date,
        "time_end": end_date,
        "limit": 1  # We only need the data for one day, exactly 4 years ago
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        data = response.json()

        if response.status_code != 200:
            error_message = data.get('error', 'Unknown error fetching historical data from CoinAPI')
            raise Exception(f"Error fetching historical data from CoinAPI: {error_message}")

        if data:
            price_4_years_ago = data[0]["price_open"]
            return price_4_years_ago
        else:
            raise Exception("No historical price data found for the specified date")


async def fetch_bitcoin_price_8_years_ago(api_key: str, currency: str = "USD") -> float:
    # Calculate the date 4 years ago from the current date
    eight_years_ago_start = datetime.datetime.now() - datetime.timedelta(days=8*365)
    # Adjust for leap years (simplified, consider more precise adjustments for production use)
    eight_years_ago_start = eight_years_ago_start.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    start_date = eight_years_ago_start.strftime('%Y-%m-%dT%H:%M:%S')
    # Assuming we want the price for the entire day, the end date is the next day
    end_date = (eight_years_ago_start + datetime.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')

    # Adjust the symbol_id as needed for your specific data source and currency
    symbol_id = f"BITSTAMP_SPOT_BTC_{currency}"

    url = f"https://rest.coinapi.io/v1/ohlcv/{symbol_id}/history"
    headers = {
        "X-CoinAPI-Key": api_key,
    }
    params = {
        "period_id": "1DAY",  # Daily data is what we're after
        "time_start": start_date,
        "time_end": end_date,
        "limit": 1  # We only need the data for one day, exactly 8 years ago
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        data = response.json()

        if response.status_code != 200:
            error_message = data.get('error', 'Unknown error fetching historical data from CoinAPI')
            raise Exception(f"Error fetching historical data from CoinAPI: {error_message}")

        if data:
            price_8_years_ago = data[0]["price_open"]
            return price_8_years_ago
        else:
            raise Exception("No historical price data found for the specified date")
        

async def fetch_bitcoin_price_12_years_ago(api_key: str, currency: str = "USD") -> float:
    # Calculate the date 4 years ago from the current date
    twelve_years_ago_start = datetime.datetime.now() - datetime.timedelta(days=12*365)
    # Adjust for leap years (simplified, consider more precise adjustments for production use)
    twelve_years_ago_start = twelve_years_ago_start.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    start_date = twelve_years_ago_start.strftime('%Y-%m-%dT%H:%M:%S')
    # Assuming we want the price for the entire day, the end date is the next day
    end_date = (twelve_years_ago_start + datetime.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')

    # Adjust the symbol_id as needed for your specific data source and currency
    symbol_id = f"BITSTAMP_SPOT_BTC_{currency}"

    url = f"https://rest.coinapi.io/v1/ohlcv/{symbol_id}/history"
    headers = {
        "X-CoinAPI-Key": api_key,
    }
    params = {
        "period_id": "1DAY",  # Daily data is what we're after
        "time_start": start_date,
        "time_end": end_date,
        "limit": 1  # We only need the data for one day, exactly 8 years ago
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        data = response.json()

        if response.status_code != 200:
            error_message = data.get('error', 'Unknown error fetching historical data from CoinAPI')
            raise Exception(f"Error fetching historical data from CoinAPI: {error_message}")

        if data:
            price_12_years_ago = data[0]["price_open"]
            return price_12_years_ago
        else:
            raise Exception("No historical price data found for the specified date")