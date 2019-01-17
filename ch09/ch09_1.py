#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
拖拽

在GUI里，拖放是指用户点击一个虚拟的对象，拖动，然后放置到另外一个对象上面的动作。

一般情况下，需要调用很多动作和方法，创建很多变量。

拖放能让用户很直观的操作很复杂的逻辑。

一般情况下，我们可以拖放两种东西：
    数据和图形界面。

把一个图像从一个应用拖放到另外一个应用上的实质是操作二进制数据。

把一个表格从Firefox上拖放到另外一个位置 的实质是操作一个图形组。

"""

"""
简单的拖放

本例使用QLineEdit 和 QPushButton
把一个文本从编辑框里拖到按钮上，更新按钮上的标签（文字）
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit



class Button(QPushButton):
    
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

        # 激活组件的拖拽事件
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        """
        我们重构了dragEnterEvent()方法。
        设定好接受拖拽的数据类型（plain text）
        """
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        """
        重构dropEvent()方法，更改按钮接受鼠标的释放事件的默认行为
        """
        self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('Button', self)
        button.move(190, 65)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Simple drag and drop')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

