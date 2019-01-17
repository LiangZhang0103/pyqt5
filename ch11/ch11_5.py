#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys, random
import matplotlib
matplotlib.use('Qt5Agg')        # Use QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# GUI 上通过控件呈现matplotlib画出来的图形 -- 通过QtWidgets.QGraphicsView控件来实现
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

# 通过继承FigureCanvas类，使得该类既是一个PyQt5的QWidget,又是一个matplotlib的FigureCanvas,
# 这是连接PyQt5与matplotlib的关键
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # 创建一个Figure, 注意：该Figure为matplotlib下的figure, 不是matplotlib.pyplot
        # 下面的figure
        fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(fig)

        self.setParent(parent)

        # 调用figure 下面的add_subplot方法，类型于matplotlib.pyplot下面的subplot
        self.axes = fig.add_subplot(111)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.plot()

    def plot(self):
        
        x = [i for i in range(1, 10)]
        y = [random.randint(1, 100) for _ in range(9)]
        self.axes.plot(x, y, 'r-')
        self.axes.set_title('PyQt5 Matplotlib Example')
        # self.draw()


class ApplicationMat(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 Matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):

        m = PlotCanvas(self, width=5, height=4)
        m.move(20, 20)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip("This is an example button")
        button.move(500, 0)
        button.resize(140, 100)

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ApplicationMat()
    sys.exit(app.exec_())


