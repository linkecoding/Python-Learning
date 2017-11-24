#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# 连接到sqlite数据库,数据库名是test.db
# 如果文件不存在会自动在当前目录创建
# conn = sqlite3.connect('test.db')
# # 创建一个Cursor
# cursor = conn.cursor()
# # 执行sql语句,创建user表
# cursor.execute(
#     'create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一条数据
# cursor.execute('insert into user (id, name) values (\'1\', \'Mich\')')
# print(cursor.rowcount)
# cursor.close()
# # 提交事务
# conn.commit()
# # 关闭连接
# conn.close()


# 插入记录
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
