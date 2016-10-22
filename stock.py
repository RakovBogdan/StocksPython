import quandl
from itertools import chain

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
            self.list_prices = list(chain.from_iterable(self.prices.values))
            self.pct_change = self.prices['Adj_Close'].pct_change().dropna()
            self.pct_change.rename(columns={'Adj_Close': self.ticker}, inplace=True)
        except Exception as e:
            print(e)

    def calc_coef(self):
        self.mean = self.pct_change.mean()
