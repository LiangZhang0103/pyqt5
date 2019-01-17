#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we display the x and y coordinates of a mouse pointer in a 
label widget.
事件对象是用python来描述一系列的事件自身属性的对象。

Author: Jan
Website: zetcode.com
Last Edited: 2018
"""

import sys 
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel 
from PyQt5.QtCore import Qt 

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x, y = 0, 0
        self.text = "x: {0}, y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        # 鼠标追踪默认没有开启，当有鼠标点击事件发生后才会开启。
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    # e代表了事件对象。里面有我们触发事件（鼠标移动）的事件对象。
    def mouseMoveEvent(self, e):

        # x()和y()方法得到鼠标的x和y坐标点
        x, y = e.x(), e.y()
        text = "x: {0}, y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())