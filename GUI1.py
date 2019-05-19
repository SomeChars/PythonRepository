#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as Qw
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot

class MyFirstGUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 250)
        self.move(300, 300)
        self.setWindowTitle('RespectTerminal')

        self.goBtn = Qw.QPushButton('Press "F" to pay respects', self)
        self.goBtn.move(150, 50)
        self.goBtn.clicked.connect(self.respectPayment)

        self.quitBtn = Qw.QPushButton('Quit', self)
        self.quitBtn.move(150, 200)
        self.quitBtn.clicked.connect(self.close)

        self.show()

    @pyqtSlot(bool)
    def respectPayment(self):
        print("Respect paid. Thank you Sir.")


if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)
    w = MyFirstGUI()
    sys.exit(app.exec_())