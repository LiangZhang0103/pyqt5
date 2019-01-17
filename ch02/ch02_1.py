#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial


This program ***creates a statusBas***.

Author: Jan
Website: zetcode.com
Last Editor: 2018
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('StatusBar')

        # 调用QtWidgets.QMainWindow类的statusBar()方法，创建状态栏.
        # 第一次调用创建一个状态栏，返回一个状态栏对象。
        # howMessage()方法在状态栏上显示一条信息
        self.statusBar().showMessage('Ready')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
