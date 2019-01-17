#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we select a font name and change the font of label.

Author: Jan
Wesite: zetcode.com
Last Edited: 2018-12-13
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, 
    QFontDialog, QSizePolicy)
import sys 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lb1 = QLabel('Knowledge only matters', self)
        self.lb1.move(130, 20)

        vbox.addWidget(btn)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 290, 180)
        self.setWindowTitle('Font Dialog')
        self.show()

    def showDialog(self):

        font, ok = QFontDialog.getFont()

        if ok:
            self.lb1.setFont(font)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())