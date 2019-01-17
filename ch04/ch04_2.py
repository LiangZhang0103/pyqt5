#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

"""
ZetCode PyQt5 tutorial
重构事件处理器


In this example. we reimplement an event handler.
在PyQt5中，事件处理器经常被重写（也就是用自己的覆盖库自带的）。

Author: Jan
Website: zetcode.com
Last Edited: 2018
"""

import sys 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    # 替换了事件处理器函数keyPressEvent()
    # 如果按下ESC键程序就会退出。
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())