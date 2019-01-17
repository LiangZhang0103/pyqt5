#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program ***creates a menuBar***.
The menuBar has one menu with an exit action.

Author: Jan
Website: zetcode.com
Last Editor: 2018
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        # QAction是菜单栏、工具栏或者快捷键的动作的组合。
        # 前面两行，我们创建了一个图标、一个exit的标签和一个快捷键组合，
        # 都执行了一个动作。
        # 第三行，创建了一个状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态。
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        # 当执行这个指定的动作时，就触发了一个事件。这个事件跟QApplication的quit()
        # 行为相关联，这个动作就能终止这个应用
        exitAct.triggered.connect(qApp.quit)

        openAct = QAction(QIcon('open.png'), '&Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open File')
        # ..... open file dialog

        self.statusBar()

        # menuBar()创建菜单栏。这里创建了一个菜单栏，
        # 并在上面添加了一个file菜单，并关联了点击退出应用的事件。
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(openAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



