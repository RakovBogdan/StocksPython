import portfolioopt as pfopt
import math
import matplotlib.pyplot as plt


class MarkowitzPortfolio:
    def __init__(self, stocks_data):
        """
        returns is pandas.DataFrame
        target_ret is floating point of expected return of the investor
        weights is pandas.Series
        """
        self.stocks_data = stocks_data
        self.returns = stocks_data.gathered_returns
        self.ret = 0.0
        self.std = 0.0
        self.annual_return_pct = 0.0
        self.annual_relative_std = 0.0
        self.annual_std_pct = 0.0
        self.avg_rets = self.returns.mean()
        self.cov_mat = self.returns.cov()
        self.weights = None

    def calculate_portfolio(self, target_return):
        """
        we get year target return in %,
        so its necessary to convert it to clear numbers
        convert to monthly, because data is collapsed by monthly
        """
        target_ret = target_return / (100 * 12)
        self.weights = pfopt.markowitz_portfolio(
            self.cov_mat, self.avg_rets, target_ret)

    def calculate_best_tangency_portfolio(self):
        self.weights = pfopt.tangency_portfolio(self.cov_mat, self.avg_rets)
        self.calculate_returns_stds()

    def calculate_returns_stds(self):
        self.ret = (self.weights * self.avg_rets).sum()
        self.std = (self.weights * self.returns).sum(1).std()
        self.annual_relative_std = (self.std * math.sqrt(12) * 100) / (self.ret * 12)
        self.annual_return_pct = (self.weights * self.avg_rets).sum() * 12 * 100
        self.annual_std_pct = self.std * math.sqrt(12) * 100

    def plot_portfolio(self):
        self.weights.index = [stock.ticker for stock in self.stocks_data.stocks]
        self.weights.name = 'Markovitz Portfolio'
        self.weights.plot.pie(
            subplots=True, figsize=(6, 6), fontsize=20, autopct='%.2f')
        plt.show()
