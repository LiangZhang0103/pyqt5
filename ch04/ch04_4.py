#!/usrr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we determine the event sender object.
想知道是哪个组件发出了一个信号，PyQt5里的sender()方法能搞定这件事。

Author: Jan
Website: zetcode.com
Last Edited: 2018
"""

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())