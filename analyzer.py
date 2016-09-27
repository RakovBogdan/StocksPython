import quandl
from stock import Stock
quandl.ApiConfig.api_key = 'dgcHTAzfi_MGZNLZvzxS'


class Analyzer:
    # start_date and end_date formta is yyyy-mm-dd
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.stocks = {}

    def addStock(self, ticker):
        self.stocks[ticker] = Stock(
            ticker, self.start_date, self.end_date)
        self.stocks[ticker].load_data()


if __name__ == '__main__':
    analyzer = Analyzer("2012-01-01", "2016-01-01")
    analyzer.addStock('BA')
    analyzer.addStock('AAPL')
    for stock in analyzer.stocks:
        print stock
