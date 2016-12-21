from itertools import chain
import pandas as pd


class Stock:
    def __init__(self, ticker, start_date, end_date):
        """start_date and end_date format is 'yyyy-mm-dd'"""
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.prices = None
        self.list_prices = None
        self.pct_change = None

    def load_data(self):
        # start_dt = datetime.strptime(self.start_date, "%y-%m-%d")
        # end_dt = datetime.strptime(self.end_date, "%y-%m-%d")
        base_url = "http://ichart.yahoo.com/table.csv?"

        year_start, month_start, day_start = self.start_date.split('-')
        year_end, month_end, day_end = self.end_date.split('-')
        # for some reason, month in yahoo starts with 0 so we have to substract 1
        month_start = str(int(month_start) - 1)
        month_end = str(int(month_end) - 1)

        params_for_url = "s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&g=m&ignore=.csv".format(
            self.ticker, month_start, day_start, year_start, month_end, day_end, year_end
        )
        try:
            # take only Adj Close and revert the dataframe
            self.prices = pd.read_csv(base_url + params_for_url,
                                      index_col=0,
                                      parse_dates=True).iloc[:, -1:].iloc[::-1]
            self.prices.rename(columns={'Adj Close': 'Adj_Close'}, inplace=True)
            self.list_prices = list(chain.from_iterable(self.prices.values))
            self.pct_change = self.prices['Adj_Close'].pct_change().dropna()
            self.pct_change.rename(columns={'Adj_Close': self.ticker}, inplace=True)
        except Exception as e:
            print(e)
