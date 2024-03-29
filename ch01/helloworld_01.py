#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Zetcode PyQt5 Tutorial

This example shows an icon in the titlebar of the window.

添加标题图标

author: Jan Bodnar
Website：zetcode.com
Last Editor: 2018
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())