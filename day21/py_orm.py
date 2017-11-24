#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()


# 定义User类
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


username = input('username:')
password = input('password:')
host = input('host:')
database = input('database:')
# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://%s:%s@%s:3306/%s' %
                       (username, password, host, database))
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()
# 创建新的User对象
user = User(id='3', name='Bob')
session.add(user)
session.commit()
session.close()

session = DBSession()
# 创建查询
user2 = session.query(User).filter(User.id == '3').one()
print('type:', type(user2))
print('name:', user2.name)
session.close()
