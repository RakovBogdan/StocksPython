import quandl


class Stock:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def load_data(self):
        try:
            self.prices = quandl.get(
                "EOD/%s.11" % self.ticker,
                start_date=self.start_date,
                end_date=self.end_date,
                collapse='monthly')
        except Exception as e:
            print(e)
