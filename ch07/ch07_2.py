#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
行编辑
QLineEdit 组件提供了编辑文本的功能， 自带撤销、重做、剪切、粘贴、拖拽等功能

"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QWidget

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.lb1 = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lb1.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):

        self.lb1.setText(text)
        self.lb1.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


