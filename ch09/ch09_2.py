#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
拖放按钮组件

例子展示怎么拖放一个button组件。

In this program, we can press on a button with a left mouse click
or drap and drop  the button with the right mouse click
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class Button(QPushButton):
    """
    从QPushButton继承一个Button类，然后重构QPushButton的两个方法
    mouseMoveEvent()和mousePressEvent().
    mouseMoveEvent()是拖拽开始的事件。
    """
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

    def mouseMoveEvent(self, e):

        # 只劫持按钮的右键事件，左键的操作还是默认行为
        if e.buttons() != Qt.RightButton:
            return

        # 创建一个QDrag对象，用来传输MIME-based数据
        mimiData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimiData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        # 拖放事件开始时，用到的处理函数是 start()
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        """
        左键点击按钮，会在控制台输出“press”。
        注意，我们在父级上也调用了mousePressEvent()方法，
        不然的话，我们是看不到按钮按下的效果的
        """
        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('Press')



class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setAcceptDrops(True)
        
        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setGeometry(300, 300, 280, 150)
        self.setWindowTitle('Click or Move')
        self.show()

    def dragEnterEvent(self, e):

        e.accept()

    def dropEvent(self, e):
        # 定义了按钮按下后和释放后的行为，获得鼠标移动的位置，然后把按钮放到这个地方
        position = e.pos()
        self.button.move(position)

        # 指定放下的动作类型为moveAction
        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

















