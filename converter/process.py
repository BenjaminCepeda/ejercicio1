import logging
from django.http import HttpResponse
from yahoofinancials import YahooFinancials
from .models import Currencies
import datetime


def query_currencies(request):
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )
    currencies = ['EURUSD=X', 'CLP=X', 'PEN=X']
    yahoo_financials_currencies = YahooFinancials(currencies)
    start_date = "2021-09-01"
    end_date = "2021-09-05"
    currencies = yahoo_financials_currencies.get_historical_price_data(
        start_date, end_date, "daily")
    logging.debug(currencies)
    for currency in currencies:
        for d in currencies[currency]['prices']:
            c = Currencies(query_date=datetime.datetime.fromtimestamp(d['date']), currency=currency.replace("=X",""), final_quote=d['close'])
            c.save()
    return HttpResponse("Start Currencies")

