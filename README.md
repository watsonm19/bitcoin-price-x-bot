# Bitcoin Price Update App

The Bitcoin Price Tracker App is a Python script designed to fetch historical Bitcoin prices, calculate their percentage changes relative to the current price, and post these updates to Twitter. This app is perfect for Bitcoin hodlers, traders, and anyone interested in the financial performance of Bitcoin over time.

## Features

- Fetches current and historical Bitcoin prices from CoinAPI and CoinMarketCap.
- Calculates the percentage change in Bitcoin's price at various intervals: start of current year, 4 years, 8 years, and 12 years.
- Posts these updates to Twitter, providing a quick and informative snapshot of Bitcoin's performance.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+ installed on your machine.
- API keys for CoinAPI, CoinMarketCap, and Twitter API v2.
- A `.env` file in your project directory with your API keys and Twitter access tokens.
