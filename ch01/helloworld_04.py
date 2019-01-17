#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial


This program shows a confirmation message box when we click on the close
button of the application window.

默认情况下，我们点击标题栏的×按钮，QWidget就会关闭。
但是有时候，我们修改默认行为。比如，如果我们打开的是一个文本编辑器，
并且做了一些修改，我们就会想在关闭按钮的时候让用户进一步确认操作。

author: Jan
Website: zetcode.com
Last Editor: 2018
"""

import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Message box")
        self.show()

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())