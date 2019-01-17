
# -*- coding:utf-8 -*-

"""
nameFile: login_ui.py

"""

from PyQt5.QtWidgets import (QApplication, QPushButton, QLabel, QLineEdit, QDialog,
                             QHBoxLayout, QVBoxLayout, QStyleFactory)
import sys


class LoginUi(QDialog):
    def __init__(self):
        super(LoginUi, self).__init__()

        self.initUI()

    def initUI(self):

        self.label_user = QLabel()
        self.label_user.setText("用户名：")
        self.lineEdit_user = QLineEdit()

        self.label_password = QLabel()
        self.label_password.setText("密码：  ")
        self.lineEdit_password = QLineEdit()

        self.pushButton_signin = QPushButton()
        self.pushButton_signin.setText("登陆")
        self.pushButton_signup = QPushButton()
        self.pushButton_signup.setText("注册")

        self.h_layout_user = QHBoxLayout()
        self.h_layout_password = QHBoxLayout()
        self.h_layout_button = QHBoxLayout()
        self.v_layout_all = QVBoxLayout()

        self.h_layout_user.addWidget(self.label_user)
        self.h_layout_user.addWidget(self.lineEdit_user)

        self.h_layout_password.addWidget(self.label_password)
        self.h_layout_password.addWidget(self.lineEdit_password)

        self.h_layout_button.addWidget(self.pushButton_signin)
        self.h_layout_button.addWidget(self.pushButton_signup)

        self.v_layout_all.addLayout(self.h_layout_user)
        self.v_layout_all.addLayout(self.h_layout_password)
        self.v_layout_all.addLayout(self.h_layout_button)

        self.setLayout(self.v_layout_all)


        self.setWindowTitle("登陆界面")
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        # QApplication.setStyle("Fusion")
        # self.setGeometry()
        self.show()

# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ui = LoginUi()
#     sys.exit(app.exec_())
































