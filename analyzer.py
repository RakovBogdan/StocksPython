import quandl
import pandas as pd
from stock import Stock
import matplotlib.pyplot as plt


quandl.ApiConfig.api_key = open('auth.txt', 'r').read()


class Analyzer:
    # start_date and end_date format is yyyy-mm-dd
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.stocks = []

    def add_stock(self, ticker):
        stock = Stock(
            ticker, self.start_date, self.end_date)
        stock.load_data()
        self.stocks.append(stock)

    def gather_stocks_returns(self):
        """collects stocks return dataframes into single dataframe gathered_returns"""
        stock_returns_list = []
        for stock in self.stocks:
            stock_returns_list.append(stock.pct_change)
        self.gathered_returns = pd.concat(stock_returns_list, axis=1)

    def plot_stocks(self, pct=False):
        if pct == False:
            for stock in self.stocks:
                ax = stock.prices['Adj_Close'].plot(label=stock.ticker)
                plt.legend(loc=2, fontsize=14)
            ax.set_ylabel('Adjusted Close')
        else:
            for stock in self.stocks:
                ax = (stock.pct_change * 100).plot(label=stock.ticker)
                plt.legend(loc=2, fontsize=14)
            ax.set_ylabel('% Change')
        plt.show()


if __name__ == '__main__':
    analyzer = Analyzer("2012-01-01", "2016-01-01")
    analyzer.add_stock('BA')
    analyzer.add_stock('AAPL')
    analyzer.gather_stocks_returns()
    print(analyzer.gathered_returns)
