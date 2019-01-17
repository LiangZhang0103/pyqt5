#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
对话框
对话框是一个现代GUI应用不可或缺的一部分。
对话是两个人之间的交流，对话框就是人与电脑之间的对话。
对话框用来输入数据，修改数据，修改应用设置等等。

输入文字
QInputDialog 提供了一个简单方便的对话框， 可以输入字符串，数字，或列表。

ZetCode PyQt5 tutorial

In this example. we receive data from a QInputDialog dialog.

Author: Jan
Website:zetcode.com
Last Edited:2018
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)
import sys 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Input dialog")
        self.show()
    
    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))

        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())