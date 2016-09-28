import quandl


class Stock:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def load_data(self):
        self.prices = quandl.get(
            "EOD/%s" % self.ticker,
            start_date=self.start_date,
            end_date=self.end_date)
