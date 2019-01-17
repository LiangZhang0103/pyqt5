#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
绘图
PyQT5 绘图系统能渲染矢量图像、位图图像和轮廓字体文本。
一般会使用再修改或者提高现有组件的功能，或者创建自己的组件。
使用PyQT5 的绘图API 进行操作。

绘图由 paintEvent() 方法完成，绘图的代码要放在 QPainter 对象的 begin() 和 end() 方法之间。
是低级接口。

"""

"""
1. 文本涂鸦

画一些Unicode文本开始

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Drawing text")
        self.show()

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):

        qp.setPen(QColor(255, 34, 2))
        qp.setFont(QFont('Decorative', 15))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






















