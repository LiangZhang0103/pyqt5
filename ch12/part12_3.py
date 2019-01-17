#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Custom colors


如果你喜欢一个样式，但想改变它的颜色， 你可以使用QPalette 和 app.setPalette(...)
"""

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        QApplication.setStyle("Fusion")
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.red)
        QApplication.setPalette(palette)

        self.button = QPushButton("&Hello World!", self)
        # self.button.setFlat(True)
        self.button.move(20, 20)


        # button.show()
        self.setWindowTitle("Custom colors")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())