#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ZetCode PyQt5 tutorial


In this example, we create a more complicated window layout using the 
QGridLayout mananger.

Author: Jan
Website: zetcode.com
Last Edited: 2018
"""

import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QLabel, QTextEdit, 
    QGridLayout)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        # 创建标签之间的空间。
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        # 我们可以指定组件的跨行和跨列的大小。这里我们指定这个元素跨5行显示。
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())