import portfolioopt as pfopt


class MarkowitzPortfolio:
    def __init__(self, returns, target_ret):
        """
        returns is pandas.DataFrame
        target_ret is floating point of expected return of the investor
        weights is pandas.Series
        """
        self.returns = returns
        self.target_ret = target_ret
        self.ret = 0.0
        self.variance = 0.0
        self.avg_rets = self.returns.mean()
        self.cov_mat = self.returns.cov()
        self.weights = None

    def create_porfolio(self):
        self.weights = pfopt.markowitz_portfolio(
            self.cov_mat, self.avg_rets, self.target_ret)
        self.ret = (self.weights * self.avg_rets).sum()
        self.variance = (self.weights * self.returns).sum(1).std()
