#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
控件2
本章节继续介绍PyQt5控件。
QPixmap, QLineEdit, QSplitter, QComBox.
"""

"""
图片
QPixmap 是处理图片的组件. 本例中，我们使用QPixmap在窗口里显示一张图片。
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap('pixmap.png')

        lb1 = QLabel(self)
        lb1.setPixmap(pixmap)

        hbox.addWidget(lb1)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())























