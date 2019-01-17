#!/usr/bin/env python3
# -*- coding:uf-8 -*-

# 1. 连接数据库
# 1.1. 导入库文件
from PyQt5.QtWidgets import QApplication
# QtSql类即QT中的QSqlDatabase类，用于处理与数据库的连接
# QSqlQuery类提供了执行和操作SQL语句的方法
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlQuery as query

# 1.2. 连接sqlite数据库
database = QSqlDatabase.addDatabase("QSQLITE")
database.setDatabaseName('user.db')

# 没有user.db这个文件时，则会在当前目录新建一个user.db文件
# 打开数据库，打开成功返回True

database.open()


# 2. 新建表
# 新建一个名为student的表，包含id, name, age 三个属性, 其中ID为主键

query.prepare('create table student (id int primary key, name varchar(30), age int)')
if not query.exec_():
    query.lastError()
else:
    print('create a table')


# 3. 插入数据
# addBindValue()将值添加到列表中，调用顺序决定添加的顺序

insert_sql = 'insert into student values (?, ?, ?)'
query.prepare(insert_sql)
query.addBindValue(4)
query.addBindValue('test3')
query.addBindValue(1)
if not query.exec_():
    print(query.lastError())
else:
    print('inserted')


# 4. 查询
# 查询返回数据使用value(int)函数，例如select id, name, age from student value(0) 等于返回id属性的值, value(2) 等于age熟悉
# exec_() 查询成功返回true查询 否则返回false

query.prepare('select id, name, age from student')
if not query.exec_():
    query.lastError()
else:
    while query.next():
        # id = query.value(0)
        # name = query.value(1)
        # age = query.value(2)
        id, name, age = query.value(0), query.value(1), query.value(2)
        print(id, name, age)

# 可以通过record().indexOf(str)来获取索引值

if query.exec('select id, name, age from student'):
    id_index = query.record().indexOf('id')
    name_index = query.record().indexOf('name')
    age_index = query.record().indexOf('age')
    while query.next():
        id = query.value(id_index)
        name = query.value(name_index)
        age = query.value(age_index)
        print(id, name, age)


# 一、使用exec()操作
# 指令执行成功则exec_()会返回True 并把查询状态设为活跃状态，否则返回false

# 另外对于SQLite, 查询字符串一次智能查询一条语句，如果给出多条语句，则函数返回false

if query.exec('select id, name, age from student'):
    while query.next():
        id, name, age = query.value(0), query.value(1), query.value(2)
        print(id, name, age)


# 二、execBatch()操作
# 这个函数是批处理之前准备好的指令，如果函数库不支持批处理他会自己调用exec()来模拟

query.prepare('insert into student values (?, ?, ?)')
query.addBindValue([6, 7, 8])
query.addBindValue(['test5', 'test6', 'test7'])
query.addBindValue([1, 1, 1])
if query.execBatch():
    print('inserted')


# 三、executedQuery()返回最后一个执行成功的指令

if query.exec('select id, name, age from student'):
    while query.next():
        id, name, age = query.value(0), query.value(1), query.value(2)
        print(id, name, age)

print(query.executedQuery())

# 执行结果为： select id, name, age from student


# 四、其它

# finish() 终止当前的操作
# isActive() 返回当前是否处于活跃状态
# isNull(int field) 返回当前是否不活跃
# isSelect() 返回是不是一个查询语句

# next() 检索结果中的下一条记录(如果可用)，并将该查询放在检索到的记录上。
# 请注意，结果必须处于活动状态，并且在调用此函数之前， isSelect() 必须返回true, 否则它将不执行任何操作并返回false.

# 指令执行成功则 exec_() 会返回True 并把查询状态设为活跃状态，否则返回false






















