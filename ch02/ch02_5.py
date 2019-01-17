#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial


This program creates a context menu.

Author: Jan
Website: zetcode.com
Last Edited: 2018
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, qApp

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')
        self.show()

    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction('New')
        opnAct = cmenu.addAction('Open')
        quitAct = cmenu.addAction('Quit')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
