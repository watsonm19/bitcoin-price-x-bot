import asyncio
import logging
import os
import tweepy

from calc_functions.percentages import calculate_percentage_gain_loss
from services.coinapi import (
    fetch_bitcoin_price_4_years_ago,
    fetch_bitcoin_price_at_year_start,
    fetch_bitcoin_price_8_years_ago,
    fetch_bitcoin_price_12_years_ago,
)
from services.coinmarketcap import fetch_bitcoin_price
from dotenv import load_dotenv

# Setup basic logging
logging.basicConfig(filename='bitcoin_pt_x_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# CoinAPI credentials
api_key_coinapi = os.getenv("COINAPI_API_KEY")

# CoinMarketCap credentials
api_key_cmc = os.getenv("COINMARKETCAP_API_KEY")

# Twitter API credentials
x_api_key = os.getenv("TWITTER_API_KEY")
x_api_secret_key = os.getenv("TWITTER_API_SECRET_KEY")
x_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
x_access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with the Twitter API
x_client = tweepy.Client(
    consumer_key=x_api_key,
    consumer_secret=x_api_secret_key,
    access_token=x_access_token,
    access_token_secret=x_access_token_secret
)

async def post_bitcoin_update():
    currency = "USD"

    # Get prices
    twelve_years_ago_price = await fetch_bitcoin_price_12_years_ago(api_key_coinapi, currency)
    eight_years_ago_price = await fetch_bitcoin_price_8_years_ago(api_key_coinapi, currency)
    four_years_ago_price = await fetch_bitcoin_price_4_years_ago(api_key_coinapi, currency)
    start_of_year_price = await fetch_bitcoin_price_at_year_start(api_key_coinapi, currency)
    current_price = await fetch_bitcoin_price(api_key_cmc, currency)

    # Calculate percentages
    percentage_change_12ya = calculate_percentage_gain_loss(current_price, twelve_years_ago_price)
    percentage_change_8ya = calculate_percentage_gain_loss(current_price, eight_years_ago_price)
    percentage_change_4ya = calculate_percentage_gain_loss(current_price, four_years_ago_price)
    percentage_change_ytd = calculate_percentage_gain_loss(current_price, start_of_year_price)

    try:
        tweet = (
            f"Current #Bitcoin price (USD): ${current_price:,.2f}\n\n"
            + f"January 1st price: ${start_of_year_price:,} ({percentage_change_ytd}%)\n"
            + f"4 years ago price: ${four_years_ago_price:,} ({percentage_change_4ya}%)\n"
            + f"8 years ago price: ${eight_years_ago_price:,} ({percentage_change_8ya}%)\n"
            + f"12 years ago price: ${twelve_years_ago_price:,} ({percentage_change_12ya}%)\n\n"
            + "#ZoomOut #HODL #BTC"
        )

        print(tweet)

        x_client.create_tweet(text=tweet)
        logging.info("Tweet successfully posted.")
    except Exception as e:
        logging.error(f"Error posting tweet: {e}")


if __name__ == "__main__":
    asyncio.run(post_bitcoin_update())

