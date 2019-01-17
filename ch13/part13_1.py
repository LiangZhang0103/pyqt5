#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Python3.x+Pyqt5实现访问SQLite（sqlite3）数据库

1. SQLite（sqlite3）数据库的安装。Python2.5版本及以上版本自带该数据库，所以Python3.x无需单独安装该数据库


2. Python3.x环境下访问SQLite（sqlite3）数据库，并在硬盘上建立数据库文件，有如下两种方法：

1>. Python3.x + sqlite3库。只用前述两者就可以，不用使用Pyqt5的相关类和方法，具体代码如下：

import sqlite3  # 导入 sqlite 库
# 在py代码当前目录创建sqlite数据库文件core.db，如果该文件已存在则连接它并打开它，否则创建该数据库文件并连接和打开它
db = sqlite3.connect("core.db")


参考
a. PyQt5逻辑与界面分离并用sqlite3+hashlib实现登陆界面：https://www.2cto.com/kf/201803/727866.html
b. PyQt4百行代码自制密码管理器(三)：数据库引入：https://blog.csdn.net/bigbennyguo/article/details/50776892
c. SQLite - Python：http://www.runoob.com/sqlite/sqlite-python.html


2>. Python3.x+Pyqt5。只用前述两者就可以，具体代码如下：

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5 import QtWidgets, QtSql
import sys

# 必须先创建一个应用程序对象，否则sqlite3数据库不支持PyQt5的类和方法对其进行操作
a = QtWidgets.QApplication(sys.argv)

# 打开SQLite数据库
con = QSqlDatabase.addDatabase('QSQLITE')

# 在py代码当前目录创建sqlite数据库文件data.db，如果该文件已存在则连接它，否则创建该数据库文件并连接
con.setDatabaseName('data.db')

# 打开数据库文件data.db
con.open()

参考
a. PyQt5之SQLite数据库操作（1）：https://blog.csdn.net/FanMLei/article/details/79432034
b. SQLite（sqlite3）数据库查看方法：安装软件“Navicat Premium 12.0.22（64位，sqlite等数据库文件查看器）的安装与破解”
    （我的硬盘上有保存），这样可以直接打开SQLite（sqlite3）数据库文件查看其内容；比如，上面2中创建的数据库文件 *.db ，
    就可以直接被“Navicat Premium”打开查看。

"""

# 数据库生成：
# 生成一个sqlite数据库，
# 使用sqlite的原因是简单、无需部署，
# 可以根据自己的情况酌情替换数据库和相应的模块

import sqlite3

# 在此文件所在的文件夹打开或创建数据库文件
conn = sqlite3.connect('user.db')

# 设置游标
c = conn.cursor()

# 创建一个含有id, name, password字段的表
c.execute('''CREATE TABLE user
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            password TEXT NOT NULL)''')

# python 连接数据库默认开启事务， 所以先提交
conn.commit()
# 关闭连接
conn.close()











