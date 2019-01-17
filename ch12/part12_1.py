#!/usr/bin/env python3
# -*- coding:utf-8

"""
Layouts
"""

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        topButton = QPushButton("Top")
        bottomButton = QPushButton("Button")

        layout = QVBoxLayout()
        # layout.addStretch(1)
        layout.addWidget(topButton)
        layout.addWidget(bottomButton)

        self.setLayout(layout)

        # self.setWindowTitle()
        self.show()


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())