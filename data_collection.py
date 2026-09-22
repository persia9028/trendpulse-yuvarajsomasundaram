# data_collection.py

from pytrends.request import TrendReq
import pandas as pd

def fetch_interest_over_time(keyword='Python'):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='US', gprop='')
    data = pytrends.interest_over_time()
    if not data.empty:
        data.to_csv('interest_over_time.csv')
        print(f"Interest over time data saved to interest_over_time.csv")
    else:
        print("No data found for the keyword.")

if __name__ == "__main__":
    fetch_interest_over_time()
