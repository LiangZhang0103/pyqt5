#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ZetCode PyQt5 tutorial


In this example, we position two push buttons in the buttom-right corner 
of the window.
盒布局能让程序具有更强的适应性。这个才是布局一个应用的更合适的方式。
QHBoxLayout和QVBoxLayout是基本的布局类，分别是水平布局和垂直布局。

Author: Jan
Website: zetcode.com
Last Edited: 2018
"""

import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, 
    QVBoxLayout)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # self.setLayout(hbox)        
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())