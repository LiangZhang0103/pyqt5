#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
俄罗斯方块游戏

Tetris

俄罗斯方块归类为下落块迷宫游戏。游戏有7个基本形状：S、Z、T、L、反向L、直线、方块，
每个形状都由4个方块组成，方块最终都会落到屏幕底部。

所以玩家通过控制形状的左右位置和旋转，让每个形状都以合适的位置落下,
如果有一行全部被方块填充，这行就会消失，并且得分。
游戏结束的条件是有形状接触到了屏幕顶部。


PyQt5是专门为创建图形界面产生的，里面一些专门为制作游戏而开发的组件，
所以PyQt5是能制作小游戏的。


"""

"""
开发

没有图片，所以就自己用绘画画出来几个图形。每个游戏里都有数学模型的，这个也是

开工之前：
 - 用QtCore.QBasicTimer()创建一个游戏循环

 - 模型是一直下落的
 
 - 模型的运动是以小块为基础单位的，不是按像素
 
 - 从数学意义上来说，模型就是就是一串数字而已

代码由四个类组成：Tetris, Board, Tetrominoe和Shape。

Tetris类创建游戏，Board是游戏主要逻辑。
Tetrominoe包含了所有的砖块，Shape是所有砖块的代码。

"""

import sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QDesktopWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor

class Tetris(QMainWindow):

    def __init__(self):
        super(Tetris, self).__init__()

        self.initUI()

    def initUI(self):
        """Initiates application UI"""

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        # self.tboard.


class Board(QFrame):

    msg2Statusbar = pyqtSignal(str)

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        """initiates board"""

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        pass


























