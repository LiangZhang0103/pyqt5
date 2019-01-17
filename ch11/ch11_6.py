#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys, os, random 

import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, 
    QMenu, QAction, QVBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt, QTimer 

import numpy as np 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.figure import Figure 

progName = os.path.basename(sys.argv[0])
progVersion = '0.1'

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget(as well as a FigureCanvasAgg, etc.)"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        super().__init__(fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.compute_initial_figure()

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)
        self.axes.set_title('AAAA')
        self.axes.plot(t, s)


class MyDynamicMplCanvas(MyMplCanvas):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        timer = QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4])

    def update_figure(self):
        """Build a list of 4 random integers between 0 and 10."""
        l = [random.randint(0, 10) for _ in range(4)]
        self.axes.cla()
        self.axes.plot([0, 1, 2, 3], l, 'r-')
        self.show()

    
class Application(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        
        menubar = self.menuBar()

        self.fileMenu = QMenu('&File', self)
        menubar.addMenu(self.fileMenu)

        self.quitAct = QAction('&Quit', self)
        self.quitAct.setShortcut('Ctrl+Q')
        self.quitAct.setToolTip("This is Quit action")
        self.quitAct.triggered.connect(self.fileQuit)
        self.fileMenu.addAction(self.quitAct)

        menubar.addSeparator()

        self.helpMenu = QMenu('&Help', self)
        menubar.addMenu(self.helpMenu)

        self.aboutAct = QAction('&About', self)
        self.aboutAct.setShortcut('Ctrl+H')
        self.aboutAct.setToolTip('This is a description about the software.')
        self.aboutAct.triggered.connect(self.about)
        self.helpMenu.addAction(self.aboutAct)
        
        # ===================================================

        self.main_widget = QWidget(self)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        l = QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)
        l.addWidget(dc)

        self.statusBar().showMessage("All hail matplotlib!", )

        # self.setGeometry(300, 300, 300, 300)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle('{}'.format(progName))
        self.show()

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        message = """embedding_in_qt5.py example
Copyright 2005 Florent Rougon, 2006 Darren Dale, 2015 Jens H Nielsen

This program is a simple example of a Qt5 application embedding matplotlib
canvases.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation.

This is modified from the embedding in qt4 example to show the difference
between qt4 and qt5"""
        QMessageBox.about(self, 'About', message)
    

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
