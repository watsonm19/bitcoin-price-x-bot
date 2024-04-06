import asyncio
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.calc_functions.percentages import calculate_percentage_gain_loss
from app.services.coinapi import (
    fetch_bitcoin_price_4_years_ago,
    fetch_bitcoin_price_at_year_start,
    fetch_bitcoin_price_8_years_ago,
    fetch_bitcoin_price_12_years_ago,
)
from app.services.coinmarketcap import fetch_bitcoin_price


async def main():
    # CoinAPI credentials
    api_key_coinapi = os.getenv("COINAPI_API_KEY")
    # CoinMarketCap credentials
    api_key_cmc = os.getenv("COINMARKETCAP_API_KEY")
    # Currency
    currency = "USD"
    
    twelve_years_ago_price = await fetch_bitcoin_price_12_years_ago(api_key_coinapi, currency)
    eight_years_ago_price = await fetch_bitcoin_price_8_years_ago(api_key_coinapi, currency)
    four_years_ago_price = await fetch_bitcoin_price_4_years_ago(api_key_coinapi, currency)
    start_of_year_price = await fetch_bitcoin_price_at_year_start(api_key_coinapi, currency)
    current_price = await fetch_bitcoin_price(api_key_cmc, currency)
    
    percentage_change_12ya = calculate_percentage_gain_loss(current_price, twelve_years_ago_price)
    percentage_change_8ya = calculate_percentage_gain_loss(current_price, eight_years_ago_price)
    percentage_change_4ya = calculate_percentage_gain_loss(current_price, four_years_ago_price)
    percentage_change_ytd = calculate_percentage_gain_loss(current_price, start_of_year_price)
    
    print("---- Prices ----")
    print(f"Bitcoin price 12 years ago: ${twelve_years_ago_price:.2f}")
    print(f"Bitcoin price 8 years ago: ${eight_years_ago_price:.2f}")
    print(f"Bitcoin price 4 years ago: ${four_years_ago_price:.2f}")
    print(f"Bitcoin price at the start of the year: ${start_of_year_price:.2f}")
    print(f"Current Bitcoin price: ${current_price:.2f}")
    print("---- Percent Changes ----")
    print(f"The percentage gain/loss since 12 years ago: {percentage_change_12ya}%")
    print(f"The percentage gain/loss since 8 years ago: {percentage_change_8ya}%")
    print(f"The percentage gain/loss since 4 years ago: {percentage_change_4ya}%")
    print(f"The percentage gain/loss since the start of the year is: {percentage_change_ytd}%")

# Run the async main function
asyncio.run(main())