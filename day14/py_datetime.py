# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

now = datetime.now()
print(now)

dt = datetime(2017, 12, 22, 10, 13, 10)
print(dt)
print(dt.timestamp())

# timestamp 转换为datetime
t = 1513908790.0
print(datetime.fromtimestamp(t))
# 转换为UTC标准时区的时间
print(datetime.utcfromtimestamp(t))

# str转换为datetime
cday = datetime.strptime('2017-6-1 19:23:56', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))


# datetime的加减
now = datetime.now()
print(now)
# datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
