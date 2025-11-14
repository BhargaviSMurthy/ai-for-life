import requests
from datetime import datetime, timedelta
import holidays

def fetch_fx_rate(date_str, currency):
    """
    Fetch FX rate for a single date.
    Replace the API URL with your real endpoint.
    """
    url = f"https://your-api.com/rates?date={date_str}&currency={currency}"
    response = requests.get(url)
    data = response.json()
    
    return data["rate"]    


def fetch_rates_for_range(start_date, end_date, currency, country_code="US"):
    url = f"https://your-api.com/daily-rates?start_date={start_date}&end_date={end_date}&currency={currency}"
    
    holidays_set = holidays.country_holidays(country_code)
    holidays_set.fromkeys(
        [datetime.strptime(date, "%Y-%m-%d").date() for date in holidays_set.keys()]
    )
    holidays.DEFAULT_START_YEAR = start_date.year
    holidays.DEFAULT_END_YEAR = end_date.year
    
    response = requests.get(url)
    result = response.json()
    return result["rates"]

def get_business_days(start_date, end_date, country_code="US"):
    holidays_set = holidays.country_holidays(country_code)
    holidays_set.fromkeys(
        [datetime.strptime(date, "%Y-%m-%d").date() for date in holidays_set.keys()]
    )
    holidays.DEFAULT_START_YEAR = start_date.year
    holidays.DEFAULT_END_YEAR = end_date.year    
    business_days = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5 and current_date not in holidays_set:
            business_days.append(current_date)
        current_date += timedelta(days=1)
    
    return business_days
