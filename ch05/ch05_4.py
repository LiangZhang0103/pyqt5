#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
选择文件
QFileDailog 给用户提供文件或者文件夹选择的功能。能打开和保存文件。

ZetCode: Jan
WebSite: zetcode.com
Last Edited: 2018-12-14(五)
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QTextEdit, QFileDialog
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.statusBar()
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'rb')

            with f:
                data = f.read()
                self.textEdit.setText(data.decode('UTF-8'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())














