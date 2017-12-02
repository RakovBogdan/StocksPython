import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import Ui_MainForm
from stocks_data import StocksData
from markowitz_portfolio import MarkowitzPortfolio


class StocksAnalyzer(Ui_MainForm):
    def __init__(self, dialog):
        Ui_MainForm.__init__(self)
        self.setupUi(dialog)
        self.listViewSuggest.hide()
        self.portfolio_initialized = False
        self.pushButtonSetDates.clicked.connect(self.initialize_stocks_data)
        self.lineEditTickerInput.textChanged.connect(self.suggest_stocks)
        self.listViewSuggest.clicked.connect(self.set_ticker)
        self.pushButtonAddStock.clicked.connect(self.add_stock)
        self.pushButtonRemoveStock.clicked.connect(self.remove_stock)
        self.pushButtonPlotStocks.clicked.connect(self.plot_stocks)
        self.pushButtonEfficientFrontier.clicked.connect(self.plot_efficient_frontier)
        self.pushButtonTangencyPortfolio.clicked.connect(self.calculate_tangency_portfolio)
        self.pushButtonCalculatePortfolio.clicked.connect(self.calculate_portfolio)
        self.pushButtonPlotPortfolio.clicked.connect(self.plot_portfolio)

    def initialize_stocks_data(self):
        start_date = self.dateEditStart.date().toPyDate().strftime('%Y-%m-%d')
        end_date = self.dateEditEnd.date().toPyDate().strftime('%Y-%m-%d')
        self.data = StocksData(
            start_date, end_date)

    def suggest_stocks(self):
        self.listViewSuggest.show()
        if self.lineEditTickerInput.text() == '':
            self.listViewSuggest.hide()
        data = self.data.possible_stocks_from_query(self.lineEditTickerInput.text())
        model = SuggestTickerModel(data)
        self.listViewSuggest.setModel(model)

    def set_ticker(self, selected):
        string_from_selected = list(self.listViewSuggest.model().itemData(selected).values())[0]
        ticker = string_from_selected.split('/')[0]
        self.lineEditTickerInput.setText(ticker)
        self.listViewSuggest.hide()

    def add_stock(self):
        self.data.add_stock(self.lineEditTickerInput.text())
        self.lineEditTickerInput.setText('')
        self.listViewSuggest.hide()
        data = [stock.ticker for stock in self.data.stocks]
        model = StocksModel(data)
        self.listViewStocks.setModel(model)

    def remove_stock(self):
        self.data.remove_stock(self.listViewStocks.selectedIndexes()[0].data())
        data = [stock.ticker for stock in self.data.stocks]
        model = StocksModel(data)
        self.listViewStocks.setModel(model)

    def plot_stocks(self):
        self.data.plot_stocks()

    def plot_efficient_frontier(self):
        self.portfolio = MarkowitzPortfolio(self.data)
        self.portfolio.plot_efficient_frontier()

    def calculate_tangency_portfolio(self):
        self.portfolio.calculate_best_tangency_portfolio()
        self.lineEditCalculatedAnnualReturn.setText(
            '%.2f' % self.portfolio.annual_return_pct)
        self.lineEditCalculatedAnnualRisk.setText(
            '%.2f' % self.portfolio.annual_std_pct
        )

    def calculate_portfolio(self):
        self.portfolio.calculate_portfolio(float(self.lineEditExpectedReturn.text()))
        self.lineEditCalculatedAnnualReturn.setText(
            '%.2f' % self.portfolio.annual_return_pct)
        self.lineEditCalculatedAnnualRisk.setText(
            '%.2f' % self.portfolio.annual_std_pct
        )

    def plot_portfolio(self):
        self.portfolio.plot_portfolio()


class SuggestTickerModel(QtCore.QAbstractListModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent):
        return len(self._data)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()]


class StocksModel(QtCore.QAbstractListModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent):
        return len(self._data)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    analyzer = StocksAnalyzer(dialog)

    dialog.show()
    sys.exit(app.exec_())
