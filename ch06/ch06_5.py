#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
日历

QCalendarWidget 提供了基于月份的日历插件
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QDate

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.lb1 = QLabel(self)
        date = cal.selectedDate()
        self.lb1.setText(date.toString())

        vbox.addWidget(self.lb1)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):

        self.lb1.setText(date.toString())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())














