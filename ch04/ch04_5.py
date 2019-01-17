#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we show how to emit a custom signal.
QObject实例能发送事件信号。

Author: Jan
Website: zetcode.com
Last Edited: 2018
"""

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtCore import pyqtSignal, QObject

class Communicate(QObject):
    
    closeApp = pyqtSignal()


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
