import quandl


class Stock:
    def __init__(self, ticker, startDate, endDate):
        self.ticker = ticker
        self.startDate = startDate
        self.endDate = endDate

    def load_data(self):
        self.prices = quandl.get(
            "EOD/%s" % self.ticker,
            start_date=self.start_date,
            end_date=self.end_date)

    def __repr__(self):
        return self.prices
