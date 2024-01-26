import requests as rs
from datetime import datetime, timedelta
# I didn't apply for twilio API, just ignore it

COMMODITY = "WTI"

# Alpha API
alpha_api = "https://www.alphavantage.co/query"
alpha_api_key = "keep in secret"


# News API
News_api = "https://newsapi.org/v2/everything"
News_api_key = "keep in secret"


# news comes within 2 days
today = datetime.now().date()  # only fetch the date
date_range = today - timedelta(days=2)  # count back 2 days

alpha_commodity_parameters = {
        "function": COMMODITY,
        "interval": "daily",
        "apikey": alpha_api_key
    }

alpha_response = rs.get(url=alpha_api, params=alpha_commodity_parameters)
alpha_data = alpha_response.json()["data"]


yesterday_value = alpha_data["data"][0]["value"]
yesterday_date = alpha_data["data"][0]["date"]
before_yesterday_value = alpha_data["data"][1]["value"]

difference = float(yesterday_value) - float(before_yesterday_value)
diff_percent = round((difference / float(yesterday_value)) * 100)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if yesterday_value == '.' or before_yesterday_value == '.':
    pass

if (float(yesterday_value) > float(before_yesterday_value) * 1.05 or
        float(yesterday_value) < float(before_yesterday_value) * 0.95):
    print(f"{COMMODITY}:{up_down}{diff_percent}% at {yesterday_date}, here are some news:")

    news_parameters = {
        "q": COMMODITY,
        "from": today,
        "to": date_range,
        "language": "en",
        "sortBy": "relevancy",
        "apikey": News_api_key
    }

    news_response = rs.get(url=News_api, params=news_parameters)
    news_data_original = news_response.json()

    first_three_articles = news_data_original["articles"][:3]  # slice() function

    news_data = []

    for article in first_three_articles:
        article_data = {
                    "title": article["title"],
                    "description": article["description"],
                    "date": article["publishedAt"].split("T")[0]
                    }
        news_data.append(article_data)

    for each_article in news_data:
        print(f"Headline:{each_article["title"]}\n"
              f"Brief:{each_article["description"]}\n"
              f"Published:{each_article["date"]}")
