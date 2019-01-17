#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ZetCode PyQt5 tutorial

事件与信号  
> === signals and slots 信号与槽机制

所有的应用都是事件驱动的。事件大部分都是由用户的行为产生的，当然也有其他的事件
产生方式，比如网络的连接，窗口管理器或者定时器等。
调用应用的exec_()方法时，应用会进入主循环，主循环会监听和分发事件。

在事件模型中，有三个角色：
    - 事件源
    - 事件
    - 事件目标
事件源就是发生了状态改变的对象。
事件是这个对象状态改变的内容。
事件目标是事件想作用的目标。
事件源绑定事件处理函数，然后作用于事件目标身上。

PyQt5处理事件方面有个signal and slot机制。Signals and slots用于对象间的通讯。
事件触发的时候，发生一个signal，slot是用来被Python调用的（就是相当于事件的绑定
函数）, slot只有在事件触发的时候才能调用。

In this example, we connect a signal of a QSlider to a slot of a QLCDNumber.


Author: Jan
Website: zetcode.com
Last Edited: 2018
"""

import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QSlider, 
    QVBoxLayout)
from PyQt5.QtCore import Qt 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        # 把滑块的变化和数字的变化绑定在一起。
        # sender是信号的发送者，receiver是信号的接收者，slot是对这个信号应该做出的反应
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())