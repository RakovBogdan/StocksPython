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
        self.calculate_returns_stds()

    def calculate_best_tangency_portfolio(self):
        self.weights = pfopt.tangency_portfolio(self.cov_mat, self.avg_rets)
        self.calculate_returns_stds()

    def calculate_returns_stds(self):
        self.ret = (self.weights * self.avg_rets).sum()
        self.std = (self.weights * self.returns).sum(1).std()
        self.annual_relative_std = (self.std * math.sqrt(12) * 100) / (self.ret * 12)
        self.annual_return_pct = (self.weights * self.avg_rets).sum() * 12 * 100
        self.annual_std_pct = self.std * math.sqrt(12) * 100
        self.weights.index = [stock.ticker for stock in self.stocks_data.stocks]
        self.weights.name = 'Markowitz Portfolio'

    def add_stock(self, ticker):

        self.stocks_data.add_stock(ticker)
        self.returns = self.stocks_data.gathered_returns
        self.avg_rets = self.returns.mean()
        self.cov_mat = self.returns.cov()


    def remove_stock(self, ticker):
        self.stocks_data.remove_stock(ticker)
        self.returns = self.stocks_data.gathered_returns
        self.avg_rets = self.returns.mean()
        self.cov_mat = self.returns.cov()

    def plot_portfolio(self):
        """
        0.0001 = 0.01% is minimum percentage for weight of stock to be plotted
        """
        plot_data = self.weights[self.weights >= 0.0001]
        plot_data.plot.pie(
            subplots=True, figsize=(6, 6), fontsize=20, autopct='%.2f')
        plt.show()

    def plot_efficient_frontier(self):
        import numpy as np
        import cvxopt as opt
        from cvxopt import blas, solvers

        returns = self.stocks_data.gathered_returns.values.T
        n = len(returns)
        returns = np.asmatrix(returns)

        N = 100
        mus = [10 ** (5.0 * t / N - 1.0) for t in range(N)]

        # Convert to cvxopt matrices
        S = opt.matrix(np.cov(returns))
        pbar = opt.matrix(np.mean(returns, axis=1))

        # Create constraint matrices
        G = -opt.matrix(np.eye(n))  # negative n x n identity matrix
        h = opt.matrix(0.0, (n, 1))
        A = opt.matrix(1.0, (1, n))
        b = opt.matrix(1.0)

        # Calculate efficient frontier weights using quadratic programming
        solvers.options['show_progress'] = False
        portfolios = [solvers.qp(mu * S, -pbar, G, h, A, b)['x']
                      for mu in mus]
        # CALCULATE RISKS AND RETURNS FOR FRONTIER
        returns = [blas.dot(pbar, x) for x in portfolios]
        risks = [np.sqrt(blas.dot(x, S * x)) for x in portfolios]
        annual_returns_pct = [(x * 100 * 12) for x in returns]
        annual_risk_pct = [(y * 100 * math.sqrt(12)) for y in risks]

        plt.ylabel('Annual returns, %')
        plt.xlabel('Annual risk, %')
        plt.plot(annual_risk_pct, annual_returns_pct, 'y-o')
        plt.show()
