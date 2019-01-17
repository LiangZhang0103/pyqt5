#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
控件
控件就像是应用这座房子的一块块砖。
PyQt5有很多的控件，比如按钮，单选框，滑动条，复选框等等。
我们将介绍一些很有用的控件：QCheckBox，ToggleButton，QSlider，QProgressBar和QCalendarWidget。
"""

# QCheckBox
# QCheckBox 组件有两状态：开和关。通常和标签一起使用，用在激活和关闭一些选项的场景。

"""
ZetCode PyQt5 tutorial

In this example, a QCheckBox widget is used to toggle the title of a window.

Author: Jan
Website: zetcode.com
Last Edited: 2018-12-17
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QMainWindow
from PyQt5.QtCore import Qt

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.statusBar()

        self.cb = QCheckBox("Show title", self)
        self.cb.move(20, 20)
        self.cb.toggle()                        # 单选框选中
        self.cb.setStatusTip('Show Title')
        # 把changeTitle()方法和stateChanged信号关联起来。这样，changeTitle()就能切换窗口标题了
        self.cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("QCheckBox")
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
            # self.cb.setStatusTip('Show Title')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



























