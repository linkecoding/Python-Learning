#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 连接mysql数据库
import mysql.connector

host = input('host:')
username = input('username:')
password = input('password:')
conn = mysql.connector.connect(
    host=host, user=username, password=password, database='test')
cursor = conn.cursor()
# 创建user表
cursor.execute(
    'create table user(id varchar(20) primary key, name varchar(20))')
# 插入一行记录
cursor.execute('insert into user(id, name) values(%s, %s)', ['1', 'Micha'])
print('行数', cursor.rowcount)
# 提交事务
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
