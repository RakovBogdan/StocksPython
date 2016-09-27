import quandl


class Stock:
    def __init__(self, ticker, startDate, endDate, prices=None):
        self.ticker = ticker
        self.startDate = startDate
        self.endDate = endDate
        self.prices = prices

    def load_data(self):
        self.prices = quandl.get(
            "EOD/%s" % self.ticker,
            start_date=self.start_date,
            end_date="2015-09-27")

    def __repr__(self):
        return self.prices
