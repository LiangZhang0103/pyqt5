#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial


This program creates a checkable menu.

Author: Jan
Website: zetcode.com
Last Edited: 2018
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        # 用checkable选项创建一个能选中的菜单。
        viewStartAct = QAction('View statusBar', self, checkable=True)
        viewStartAct.setStatusTip('View statusBar')
        # 默认设置为选中状态。
        viewStartAct.setChecked(True)
        viewStartAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStartAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
