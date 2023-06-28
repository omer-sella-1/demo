import requests
from datetime import datetime, timedelta
import urllib3
import smtplib

urllib3.disable_warnings()

# Global Constants
STOCK_API_KEY = "demo"
NEWS_API_KEY = "e9c7462d4da3471f90a1482a7524b5a3"
SEND_TO = "omersella95@gmail.com"


yesterday = datetime.now().date() - timedelta(1)
before_yesterday = datetime.now().date() - timedelta(2)



class StockAnalyzer:
    """Class for analyzing stock prices."""

    def __init__(self, stock_symbol, company_name):
        self.stock_symbol = stock_symbol
        self.company_name = company_name
        self.stock_endpoint = "https://www.alphavantage.co/query"

    def get_stock_prices(self):
        """Get stock prices for yesterday and the day before yesterday."""
        stock_params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.stock_symbol,
            "apikey": STOCK_API_KEY,
        }
        data = requests.get(self.stock_endpoint, verify=False, params=stock_params).json()
        yesterday_close_price = int(data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
        before_yesterday_close_price = int(data["Time Series (Daily)"][f"{before_yesterday}"]["4. close"])
        return yesterday_close_price, before_yesterday_close_price

    def calculate_price_difference(self, yesterday_price, before_yesterday_price):
        """Calculate the difference in stock prices."""
        difference = round(abs(yesterday_price - before_yesterday_price), 2)
        return difference

    def is_price_increase(self, yesterday_price, before_yesterday_price):
        """Check if the stock price increased."""
        return yesterday_price - before_yesterday_price > 0

class NewsFetcher:
    """Class for fetching news articles."""

    def __init__(self, company_name):
        self.company_name = company_name
        self.news_endpoint = "https://newsapi.org/v2/everything"

    def get_articles(self, from_date, to_date):
        """Get news articles for the given date range."""
        news_params = {
            "q": self.company_name,
            "apiKey": NEWS_API_KEY,
            "sortBy": "popularity",
            "from": from_date,
            "to": to_date,
        }
        news_data = requests.get(self.news_endpoint, verify=False, params=news_params)
        return news_data.json()["articles"]

class EmailSender:
    """Class for sending emails."""

    def __init__(self, sender_email, sender_password, receiver_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email

    def send_email(self, subject, message):
        """Send an email with the given subject and message."""
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password=self.sender_password)
            connection.sendmail(from_addr=self.sender_email, to_addrs=self.receiver_email, msg=f"Subject: {subject}\n\n{message}")


# Main program
if __name__ == "__main__":
    my_email = "omersella25@gmail.com"
    password = "nftqbbyeuecexeen"
    STOCK = "TSLA"
    COMPANY_NAME = "Tesla Inc"

    stock_analyzer = StockAnalyzer(STOCK, COMPANY_NAME)
    yesterday_price, before_yesterday_price = stock_analyzer.get_stock_prices()
    difference = stock_analyzer.calculate_price_difference(yesterday_price, before_yesterday_price)
    difference_positive = stock_analyzer.is_price_increase(yesterday_price, before_yesterday_price)

    news_fetcher = NewsFetcher(COMPANY_NAME)
    news = news_fetcher.get_articles(before_yesterday, yesterday)

    if difference_positive:
        logo = '-'
    else:
        logo = '+'

    email_sender = EmailSender(my_email, password, SEND_TO)

    for num in range(0, 2):
        subject = f"{COMPANY_NAME}: {logo}{difference}% {news[num]['title']}"
        message = f"{news[num]['description']}"
        email_sender.send_email(subject, message)
