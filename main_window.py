# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(842, 699)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainForm.setFont(font)
        self.lineEditTickerInput = QtWidgets.QLineEdit(MainForm)
        self.lineEditTickerInput.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.lineEditTickerInput.setObjectName("lineEditTickerInput")
        self.pushButtonAddStock = QtWidgets.QPushButton(MainForm)
        self.pushButtonAddStock.setGeometry(QtCore.QRect(140, 140, 151, 31))
        self.pushButtonAddStock.setObjectName("pushButtonAddStock")
        self.pushButtonRemoveStock = QtWidgets.QPushButton(MainForm)
        self.pushButtonRemoveStock.setGeometry(QtCore.QRect(610, 270, 151, 31))
        self.pushButtonRemoveStock.setObjectName("pushButtonRemoveStock")
        self.dateEditStart = QtWidgets.QDateEdit(MainForm)
        self.dateEditStart.setGeometry(QtCore.QRect(290, 10, 131, 31))
        self.dateEditStart.setObjectName("dateEditStart")
        self.pushButtonSetDates = QtWidgets.QPushButton(MainForm)
        self.pushButtonSetDates.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.pushButtonSetDates.setObjectName("pushButtonSetDates")
        self.labelStartDate = QtWidgets.QLabel(MainForm)
        self.labelStartDate.setGeometry(QtCore.QRect(180, 15, 111, 21))
        self.labelStartDate.setObjectName("labelStartDate")
        self.labelEndDate = QtWidgets.QLabel(MainForm)
        self.labelEndDate.setGeometry(QtCore.QRect(480, 10, 91, 31))
        self.labelEndDate.setObjectName("labelEndDate")
        self.dateEditEnd = QtWidgets.QDateEdit(MainForm)
        self.dateEditEnd.setGeometry(QtCore.QRect(580, 10, 131, 31))
        self.dateEditEnd.setObjectName("dateEditEnd")
        self.labelTicker = QtWidgets.QLabel(MainForm)
        self.labelTicker.setGeometry(QtCore.QRect(10, 110, 121, 21))
        self.labelTicker.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTicker.setObjectName("labelTicker")
        self.pushButtonPlotStocks = QtWidgets.QPushButton(MainForm)
        self.pushButtonPlotStocks.setGeometry(QtCore.QRect(300, 190, 151, 41))
        self.pushButtonPlotStocks.setObjectName("pushButtonPlotStocks")
        self.pushButtonEfficientFrontier = QtWidgets.QPushButton(MainForm)
        self.pushButtonEfficientFrontier.setGeometry(QtCore.QRect(20, 350, 201, 41))
        self.pushButtonEfficientFrontier.setObjectName("pushButtonEfficientFrontier")
        self.pushButtonTangencyPortfolio = QtWidgets.QPushButton(MainForm)
        self.pushButtonTangencyPortfolio.setGeometry(QtCore.QRect(20, 400, 201, 41))
        self.pushButtonTangencyPortfolio.setObjectName("pushButtonTangencyPortfolio")
        self.pushButtonCalculatePortfolio = QtWidgets.QPushButton(MainForm)
        self.pushButtonCalculatePortfolio.setGeometry(QtCore.QRect(20, 560, 151, 31))
        self.pushButtonCalculatePortfolio.setObjectName("pushButtonCalculatePortfolio")
        self.labelExpectedReturnPortfolio = QtWidgets.QLabel(MainForm)
        self.labelExpectedReturnPortfolio.setGeometry(QtCore.QRect(0, 310, 841, 31))
        self.labelExpectedReturnPortfolio.setAlignment(QtCore.Qt.AlignCenter)
        self.labelExpectedReturnPortfolio.setObjectName("labelExpectedReturnPortfolio")
        self.lineEditExpectedReturn = QtWidgets.QLineEdit(MainForm)
        self.lineEditExpectedReturn.setGeometry(QtCore.QRect(20, 520, 121, 31))
        self.lineEditExpectedReturn.setObjectName("lineEditExpectedReturn")
        self.labelSetExpectedReturn = QtWidgets.QLabel(MainForm)
        self.labelSetExpectedReturn.setGeometry(QtCore.QRect(20, 480, 321, 31))
        self.labelSetExpectedReturn.setObjectName("labelSetExpectedReturn")
        self.labelCalculatedAnnualReturn = QtWidgets.QLabel(MainForm)
        self.labelCalculatedAnnualReturn.setGeometry(QtCore.QRect(530, 450, 301, 31))
        self.labelCalculatedAnnualReturn.setObjectName("labelCalculatedAnnualReturn")
        self.lineEditCalculatedAnnualReturn = QtWidgets.QLineEdit(MainForm)
        self.lineEditCalculatedAnnualReturn.setGeometry(QtCore.QRect(530, 490, 113, 31))
        self.lineEditCalculatedAnnualReturn.setObjectName("lineEditCalculatedAnnualReturn")
        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(530, 530, 261, 31))
        self.label.setObjectName("label")
        self.lineEditCalculatedAnnualRisk = QtWidgets.QLineEdit(MainForm)
        self.lineEditCalculatedAnnualRisk.setGeometry(QtCore.QRect(530, 570, 113, 31))
        self.lineEditCalculatedAnnualRisk.setObjectName("lineEditCalculatedAnnualRisk")
        self.pushButtonPlotPortfolio = QtWidgets.QPushButton(MainForm)
        self.pushButtonPlotPortfolio.setGeometry(QtCore.QRect(300, 610, 151, 41))
        self.pushButtonPlotPortfolio.setObjectName("pushButtonPlotPortfolio")
        self.listViewSuggest = QtWidgets.QListView(MainForm)
        self.listViewSuggest.setGeometry(QtCore.QRect(10, 160, 581, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listViewSuggest.setFont(font)
        self.listViewSuggest.setObjectName("listViewSuggest")
        self.listViewStocks = QtWidgets.QListView(MainForm)
        self.listViewStocks.setGeometry(QtCore.QRect(500, 51, 256, 211))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listViewStocks.setFont(font)
        self.listViewStocks.setObjectName("listViewStocks")
        self.lineEditTickerInput.raise_()
        self.pushButtonAddStock.raise_()
        self.pushButtonRemoveStock.raise_()
        self.dateEditStart.raise_()
        self.pushButtonSetDates.raise_()
        self.labelStartDate.raise_()
        self.labelEndDate.raise_()
        self.dateEditEnd.raise_()
        self.labelTicker.raise_()
        self.pushButtonPlotStocks.raise_()
        self.pushButtonEfficientFrontier.raise_()
        self.pushButtonTangencyPortfolio.raise_()
        self.pushButtonCalculatePortfolio.raise_()
        self.labelExpectedReturnPortfolio.raise_()
        self.lineEditExpectedReturn.raise_()
        self.labelSetExpectedReturn.raise_()
        self.labelCalculatedAnnualReturn.raise_()
        self.lineEditCalculatedAnnualReturn.raise_()
        self.label.raise_()
        self.lineEditCalculatedAnnualRisk.raise_()
        self.pushButtonPlotPortfolio.raise_()
        self.listViewStocks.raise_()
        self.listViewSuggest.raise_()

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Stocks Analyzer"))
        self.pushButtonAddStock.setText(_translate("MainForm", "Add Stock"))
        self.pushButtonRemoveStock.setText(_translate("MainForm", "Remove Stock"))
        self.pushButtonSetDates.setText(_translate("MainForm", "Set Dates"))
        self.labelStartDate.setText(_translate("MainForm", "Start Date"))
        self.labelEndDate.setText(_translate("MainForm", "End Date"))
        self.labelTicker.setText(_translate("MainForm", "Ticker"))
        self.pushButtonPlotStocks.setText(_translate("MainForm", "Plot Stocks"))
        self.pushButtonEfficientFrontier.setText(_translate("MainForm", "Efficient Frontier"))
        self.pushButtonTangencyPortfolio.setText(_translate("MainForm", "Tangency Portfolio"))
        self.pushButtonCalculatePortfolio.setText(_translate("MainForm", "Calculate"))
        self.labelExpectedReturnPortfolio.setText(_translate("MainForm", "Excptected return portfolio"))
        self.labelSetExpectedReturn.setText(_translate("MainForm", "Set Annual Expected Return, %:"))
        self.labelCalculatedAnnualReturn.setText(_translate("MainForm", "Calculated Annual Return, %:"))
        self.label.setText(_translate("MainForm", "Calculated Annual Risk, %:"))
        self.pushButtonPlotPortfolio.setText(_translate("MainForm", "Plot Portfolio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())
