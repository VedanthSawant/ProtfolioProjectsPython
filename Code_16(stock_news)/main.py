import requests
import smtplib
from datetime import datetime, timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "P3WOA6EGFC0G9INX"
NEWS_API_KEY = "8755e4262bb14813a1493b2e30ab5ccd"
my_email = "vedsawant07@gmail.com"
my_password = "ubmqdqlttensqtce"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_respose = requests.get(STOCK_ENDPOINT, stock_parameters)
stock_respose.raise_for_status()
stock_data = stock_respose.json()

# getting yesterday and day before yesterday date from datetime module
yesterday_date = (datetime.today() - timedelta(days=1)).date()
day_before_yesterday = (datetime.today() - timedelta(days=2)).date()

# getting the closing time stock value for both days
yesterday_stock = stock_data["Time Series (Daily)"][str(yesterday_date)]["4. close"]
day_before_yesterday_stock = stock_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

# getting how much the stock has increased/decreased
stock_price_difference = "{:.4f}".format(abs(float(yesterday_stock) - float(day_before_yesterday_stock)))
percent_change = float("{:.4f}".format((float(stock_price_difference) / float(day_before_yesterday_stock)) * 100))
print(percent_change)
# checking the percentage threshold
if percent_change > 0.5:
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    new_respose = requests.get(NEWS_ENDPOINT, news_parameters)
    news_data = new_respose.json()
    news_articles = news_data["articles"][:3]

    new_dict = {}
    new_list = []
    for item in news_articles:
        title = item["title"]
        description = item["description"]
        new_dict["title"] = title
        new_dict["description"] = description
        new_list.append(new_dict)
    print(new_list)

    for item in new_list:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="vedsawant97@gmail.com",
            msg=f"Subject:{STOCK}\n\nHeadline: {item["title"]}\nBrief: {item["description"]}")
        connection.close()
