#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
下拉选框
QComBox 组件能让用户在多个选择项中选择一个。

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.lb1 = QLabel("Ubuntu", self)

        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lb1.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComBox')
        self.show()

    def onActivated(self, text):

        self.lb1.setText(text)
        self.lb1.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())









