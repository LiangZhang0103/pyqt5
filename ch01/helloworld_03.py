#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 


This program create a quit button(退出按钮). When we pree the 
button, the application terminates.


author: Jan
Website: zetcode.com
Last Editor: 2018
"""

import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
# from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        qbtn = QPushButton('Quit', self)
        """
        事件传递系统在PyQt5内建的single和slot机制里面。点击按钮之后，信号会被捕捉并给出既定的反应。
        QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，instance()创建了一个它的实例。
        QCoreApplication是在QApplication里创建的。
        点击事件和能终止进程并退出应用的quit函数绑定在了一起。
        在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。
        """
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())