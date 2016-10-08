import quandl
from stock import Stock
import matplotlib.pylab as plt



quandl.ApiConfig.api_key = open('auth.txt', 'r').read()


class Analyzer:
    # start_date and end_date formta is yyyy-mm-dd
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.stocks = []

    def add_stock(self, ticker):
        stock = Stock(
            ticker, self.start_date, self.end_date)
        stock.load_data()
        self.stocks.append(stock)


if __name__ == '__main__':
    analyzer = Analyzer("2012-01-01", "2016-01-01")
    analyzer.add_stock('BA')
    analyzer.add_stock('AAPL')
    for stock in analyzer.stocks:
        ax = stock.prices['Adj_Close'].plot(label=stock.ticker)
        plt.legend(loc=2, fontsize=14)
    ax.set_ylabel('Adjusted Close')
    plt.show()
