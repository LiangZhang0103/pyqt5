#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QFrame, QHBoxLayout, QVBoxLayout,
                             QDial, QWidget, QSizePolicy, QSpacerItem, QSpinBox, QTextBrowser, QGroupBox)
from PyQt5.QtCore import Qt, QRect, QSize, QCoreApplication
# from PyQt5.QtGui import QFont
import sys

class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 1.
        self.topGroupBox = QGroupBox()
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')

        # 1.1
        self.dial = QDial()
        self.dial.setMaximumSize(QSize(16777215, 16777215))
        self.dial.setObjectName('dial')

        self.horizontalLayout.addWidget(self.dial)

        # 1.2
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName('verticalLayout')

        # 1.2.1
        spacerItem = QSpacerItem(10, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        # 1.2.2
        self.spinBox = QSpinBox()
        self.spinBox.setObjectName('spinBox')
        self.verticalLayout.addWidget(self.spinBox)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.topGroupBox.setLayout(self.horizontalLayout)
        # self.topGroupBox.setFlat(True)

        # 2.
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName('line')

        # 3.
        self.textBrowser = QTextBrowser()
        self.textBrowser.setObjectName('textBrowser')

        # 网格布局
        self.mainLayout = QGridLayout()
        self.mainLayout.setContentsMargins(4, 4, 4, 4)
        self.mainLayout.addWidget(self.topGroupBox, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.line, 1, 0, 1, 1)
        self.mainLayout.addWidget(self.textBrowser, 2, 0, 1, 1)

        self.setLayout(self.mainLayout)


        self.setObjectName('Dialog')
        self.resize(390, 275)
        self.setSizeGripEnabled(True)
        # self.setWindowTitle("Dialog")

        self.retranslateUi()
        self.spinBox.valueChanged['int'].connect(self.dial.setValue)
        self.dial.valueChanged['int'].connect(self.spinBox.setValue)


        self.show()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    uiDialog = Ui_Dialog()
    sys.exit(app.exec_())
