#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial


This program creates a subMenu.

Author: Jan
Website: zetcode.com
Last Editor: 2018
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')

        newAct = QAction('new', self)
        fileMenu.addAction(newAct)

        impMenu = QMenu('Import', self)
        fileMenu.addMenu(impMenu)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
