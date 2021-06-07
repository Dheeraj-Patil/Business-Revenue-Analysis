import sys
import datetime
from PyQt5.QtWidgets
import QApplication, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QMessageBox
from PyQt5 import QtCore

class AppWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    alertMsg=''
    def initUI(self):

        loadcsvBtn = QPushButton("Load CSV")
        loadcsvBtn.setStyleSheet("background-color: #45CE30")
        plotBtn = QPushButton("Plot the Analysis")
        alertBtn = QPushButton("Analyse")
        multiGBtn = QPushButton("Plot Seperate Graphs")
        alertBtn.setStyleSheet("background-color: #2af7ff")
        multiGBtn.setStyleSheet("background-color: #EA425C")
        plotBtn.setStyleSheet("background-color: #c02aff")

        label =  QLabel("Load the Data and Plot Graph")
        hbox = QHBoxLayout()
        hbox.addWidget(loadcsvBtn)
        hbox.addWidget(alertBtn)
        hbox.addWidget(plotBtn)
        hbox.addWidget(multiGBtn)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        def alert():
            if self.alertMsg=='':
                QMessageBox.about(self, "Sorry for that", "Load CSV First")
            else:
                self.result()
                QMessageBox.about(self, "Your Results", self.alertMsg)

        loadcsvBtn.clicked.connect(self.read)
        plotBtn.clicked.connect(self.showGraph)
        alertBtn.clicked.connect(alert)
        multiGBtn.clicked.connect(self.plot_multi)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Best Selling Product Analyser')
        self.show()

    filePath=''
    months=''
    tv=''
    ac=''
    wm=''
    pc=''

    def plot_multi(self):
        from matplotlib import pyplot as plt
        plt.figure('Television Sales Graph')
        plt.plot(self.months, self.tv)
        plt.title('Television Sales')
        plt.xlabel("Months")
        plt.ylabel("Revenue")
        plt.show()

        plt.figure('Air Conditioner Sales Graph')
        plt.plot(self.months, self.ac)
        plt.title('Air Conditioner Sales')
        plt.xlabel("Months")
        plt.ylabel("Revenue")
        plt.show()

        plt.figure('Washing Machine Sales Graph')
        plt.plot(self.months, self.wm)
        plt.title('Washing Machine Sales')
        plt.xlabel("Months")
        plt.ylabel("Revenue")
        plt.show()

        plt.figure('Computer Sales Graph')
        plt.plot(self.months, self.pc)
        plt.title('Computer Sales')
        plt.xlabel("Months")
        plt.ylabel("Revenue")
        plt.show()

        plt.figure('Aggregated Graph')
        plt.plot(self.months, self.tv, label='TV')
        plt.plot(self.months, self.ac, label='AC')
        plt.plot(self.months, self.wm, label='WM')
        plt.plot(self.months, self.pc, label='PC')
        plt.legend()
        plt.show()

    def read(self):
        pathFileName, _ = QFileDialog.getOpenFileName(None, 'Select a CSV file to Plot', '', 'csv(*.csv)')
        self.filePath=pathFileName
        self.alertMsg='0'

    def result(self):
        import matplotlib.pyplot as plt
        import pandas as pd

        data = pd.read_csv(self.filePath)

        self.months=data['Month']
        self.tv=data['TV']
        self.ac=data['AC']
        self.wm=data['Washing Machine']
        self.pc=data['Computer']
        self.best()


    def best(self):
        self.result
        tv_s=sum(self.tv.to_list())
        ac_s=sum(self.ac.to_list())
        wm_s=sum(self.wm.to_list())
        pc_s=sum(self.pc.to_list())

        scores = {'TV': tv_s, 'Air Conditioner': ac_s, 'Washing Machine': wm_s, 'Computer': pc_s}
        sorted_s = {}
        sorted_sd = {}
        for key, value in sorted(scores.items(), key=lambda kv: kv[1], reverse=True):
            sorted_s[key] = value

        for key, value in sorted(scores.items(), key=lambda kv: kv[1], reverse=False):
            sorted_sd[key] = value

        self.alertMsg=('Best selling product: ' + str(next(iter(sorted_s))) + "\nLeast Selling Product: " + str(next(iter(sorted_sd))) )



    def showGraph(self):
        import matplotlib.pyplot as plt

        ax1 = plt.subplot(3,2,1)
        ax1.margins(0.05)
        ax1.plot(self.months,self.tv , marker='4', color='r')
        ax1.set_xlabel('Months')
        ax1.set_ylabel('Revenue in Rupees')
        ax1.set_title('TV Sales')
        ax1.text(2, 6, 'Revenue in Rs', fontsize=8)

        ax2 = plt.subplot(3,2,2)
        ax2.margins(0.1)
        ax2.plot(self.months,self.ac , marker='1', color='b')
        ax2.set_xlabel('Months')
        ax2.set_ylabel('Revenue in Rupees')
        ax2.set_title('Air Conditioner Sales')

        ax3 = plt.subplot(3,2,5)
        ax3.margins(0.1)
        ax3.plot(self.months,self.wm, marker='2', color='g')
        ax3.set_xlabel('Months')
        ax3.set_ylabel('Revenue in Rupees')
        ax3.set_title('Washing Machine Sales')

        ax4 = plt.subplot(3,2,6)
        ax4.margins(0.1)
        ax4.plot(self.months,self.pc, marker='3', color='purple')
        ax4.set_xlabel('Months')
        ax4.set_ylabel('Revenue in Rupees')
        ax4.set_title('Computer Sales')


        ax5 = plt.subplot(3,1,2)
        ax5.margins(0.05)
        ax5.set_title('All Products')
        ax5.plot(self.months, self.tv,  color='b', label='TV')
        ax5.plot(self.months, self.ac,  color='g', label='AC')
        ax5.plot(self.months, self.wm,  color='r', label='WM')
        ax5.plot(self.months, self.pc,  color='k', label='PC')
        ax5.legend()
        ax5.set_xlabel('Months')
        ax5.set_ylabel('Revenue')
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet("QPushButton { margin: 9ex; padding: 5px;} QLabel {color: #FFF222; font-size: 28px;} QWidget{ background:#333945;}")
    ex = AppWindow()
    sys.exit(app.exec_())
