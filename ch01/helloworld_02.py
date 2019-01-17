#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Zetcode PyQt5 tutorial

This example shows a tooltip(提示框) on a window and button.

Author: Jan Bodnar
Website: zetcode.com
Last Editor: 
"""

import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton 
from PyQt5.QtGui import QIcon, QFont


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        # 静态方法设置了提示框的字体
        QToolTip.setFont(QFont('SansSerif', 10))

        # 窗口提示框
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        # 按钮提示框
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # sizeHint()：按钮的默认大小
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300,200)
        self.setWindowTitle('ToolTip')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())