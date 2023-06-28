# Stock News Bot

The Stock News Bot is a Python application that analyzes stock prices and fetches related news articles for a given company. It sends an email notification with the stock price change and the top news articles to a specified recipient.

## Features

- Analyzes stock prices for a specific company
- Retrieves news articles related to the company
- Sends an email with stock price change and news articles

## Prerequisites

- Python 3.x
- Required Python packages (can be installed via pip):
  - requests
  - datetime
  - urllib3
  - smtplib

## Setup

1. Clone the repository: https://github.com/omer-sella-1/stock_news_bot/

2. Install the required Python packages: $ pip install requests datetime urllib3 smtplib

3. Update the configuration:

- Open the `main.py` file.
- Modify the following variables according to your requirements:
  - `my_email`: Your Gmail email address.
  - `password`: The password for your Gmail account.
  - `STOCK`: The stock symbol (e.g., "TSLA" for Tesla Inc).
  - `COMPANY_NAME`: The name of the company.
  - `SEND_TO`: The recipient email address.

4. Run the application: 
 pip install requests datetime urllib3 smtplib

The application will analyze the stock prices, fetch news articles, and send an email with the relevant information.
