#!/usr.bin.env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QTextBrowser, QMainWindow

# class Example(QWidget):
#     def __init__(self):
#         super(Example, self).__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         TextBr = QTextBrowser(self)
#         TextBr.setGeometry(400, 300, 300, 100)
#         TextBr.setText("Test")
#
#         btn = QPushButton('btn', self)
#
#         frm = QFrame(self)
#         frm.setGeometry(100, 0, 100, 100)
#
#         self.setGeometry(300, 200, 1000, 500)
#         self.setWindowTitle('QSS learning')
#         # 设置StyleSheet
#         self.setStyleSheet("QWidget {background-color: rgb(0, 0, 0)}")
#         self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

"""
发现所有四个对象的背景颜色全都设置成了黑色，这其实是我们不想看到的结果。
究其原因，是由于QTextBrowser, QPushButton, QFrame这三个类都继承自QWidget的缘故。
"""

# ============================================================================
# class Example(QMainWindow):
#     def __init__(self):
#         super(Example, self).__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         TextBr = QTextBrowser(self)
#         TextBr.setGeometry(400, 300, 300, 100)
#         TextBr.setText("Text")
#
#         btn = QPushButton("btn", self)
#
#         frm = QFrame(self)
#         frm.setGeometry(100, 0, 100, 100)
#
#         self.setGeometry(300, 200, 1000, 500)
#         self.setStyleSheet("QMainWindow {background-color: rgb(0, 0, 0)}")
#         self.setWindowTitle('Qss learning')
#         self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

"""
TextBr和btn得到保持，而frm依然没有显示出来。
所以此时，背景颜色变成黑色的其实只有QMainWindow类型的主窗口ex
"""


# ============================================================================

# class Example(QMainWindow):
#     def __init__(self):
#         super(Example, self).__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         TextBr = QTextBrowser(self)
#         TextBr.setGeometry(400, 300, 300, 100)
#         TextBr.setText("Text")
#
#         btn = QPushButton("btn", self)
#
#         frm = QFrame(self)
#         frm.setGeometry(100, 0, 100, 100)
#
#         self.setGeometry(300, 200, 1000, 500)
#         self.setStyleSheet("QMainWindow {background-color: rgb(255, 0, 0)}")
#         self.setStyleSheet("QPushButton {background-color:rgb(255, 255, 0)}")
#         self.setStyleSheet("QFrame {background-color:rgb(0, 255, 0)}")
#         self.setStyleSheet("QTextBrowser {background-color:rgb(255, 0, 0)}")    # QTextBrowser是继承自QFrame的
#         self.setWindowTitle('Qss learning')
#         self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

"""
设置全局QSS的入口在主窗口的setStyleSheet()函数，
在其中添加QSS语法，就可以设置此对象中所有样式。 

因为在setStyleSheet()函数中，实际输入的参数是字符串类型，
所以完全可以把QSS语法存在文档里，再用程序读取。 

qss1.txt

QMainWindow {background-color: rgb(0, 0, 0)}
QPushButton {background-color:rgb(255, 255, 0)}
QFrame {background-color:rgb(0, 255, 0)}
QTextBrowser {background-color:rgb(255, 0, 0)}

python读取时，不会是一个字符串，
所以需要一些方法，比如以下代码可以正常读取txt并将内容转化成字符串
with open('C:\\Users\\Martin\\Desktop\\qss1.txt') as file:
    strLst = file.readlines()
    str =''.join(strLst).strip('\n')
self.setStyleSheet(str)
self.show()
"""

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        TextBr = QTextBrowser(self)
        TextBr.setGeometry(400, 300, 300, 100)
        TextBr.setText("Text")

        btn = QPushButton("btn", self)

        frm = QFrame(self)
        frm.setGeometry(100, 0, 100, 100)

        self.setGeometry(300, 200, 1000, 500)
        self.setWindowTitle('Qss learning')
        with open('qss.txt') as file:
            strLst = file.readlines()
            str = ''.join(strLst).strip('\n')
        print(str)
        self.setStyleSheet(str)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())










