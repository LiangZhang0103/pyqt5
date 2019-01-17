#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Style sheets  样式表

除了上述， 你可以改变通过样式表改变应用的外观/外形。

这是Qt的CSS。 我们可以使用这个样例来增加一些空间
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setStyleSheet("QPushButton { margin: 20ex; }")

        button = QPushButton("&Hello World!", self)

        # button2 = QPushButton("&Hello World2!", self)

        self.setGeometry(300, 300, 300, 260)
        self.setWindowTitle("Style sheets")

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet("QWidget { margin: 10ex; }")
    ex = Example()
    sys.exit(app.exec_())

































