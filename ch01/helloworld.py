#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ZetCode PyQt5 tutorial

Inthis example, we create a simple 
window in PyQt5.

过程式编程

author: Jan Bodnar
website: zetcode.com
Last editor:  2018
"""

import sys
# PyQt5.QtWidgets模块，包含了基本的组件
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":

    # 每个PyQt5应用都必须创建一个应用对象; sys.argv是一组命令行列表
    # Python 在shell中运行,参数提供对脚本控制的功能
    app = QApplication(sys.argv)
    # QWidget控件是一个用户界面的基本控件，它提供了基本的应用构造器
    # 没有父级的构造器称为窗口(Window)
    w = QWidget()
    # resize()方法改变控件的大小
    w.resize(250, 150)
    # move()方法修改控件的位置
    w.move(300, 300)
    # setWindowTitle()方法：给窗口添加一个标题栏
    w.setWindowTitle("Simple")
    # show()能让控件在窗口显示
    w.show()
    
    # 进入了应用的主循环中，事件处理器这个时候开始工作。
    # 主循环从窗口上接收事件，并把事件传入到派发到应用控件里。
    # 当调用exit()方法或直接销毁主控件时，主循环就会结束。
    # sys.exit()方法能确保主循环安全退出。外部环境能通知主控件怎么结束
    sys.exit(app.exec_())