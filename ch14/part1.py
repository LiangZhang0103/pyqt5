#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
                            QGridLayout)
from PyQt5.QtCore import Qt

class AddressBook(QWidget):
    def __init__(self, parent=None):
        super(AddressBook, self).__init__(parent)

        self.initUI()

    def initUI(self):

        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()

        addressLabel = QLabel("Address:")
        self.addressText = QTextEdit()

        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0, 1, 1)
        mainLayout.addWidget(self.nameLine, 0, 1, 1, 1)
        mainLayout.addWidget(addressLabel, 1, 0, 1, 1, Qt.AlignTop)
        mainLayout.addWidget(self.addressText, 1, 1, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Simple Address Book")
        self.show()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    addressBook = AddressBook()

    sys.exit(app.exec_())
