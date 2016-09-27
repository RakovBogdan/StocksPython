import quandl
from stock import Stock
quandl.ApiConfig.api_key = 'dgcHTAzfi_MGZNLZvzxS'


class Analyzer:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.stocks = []

    def addStock(self, ticker):
        self.stocks.append(Stock(
            ticker, self.start_date, self.end_date)
        
