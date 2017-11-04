#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

# 枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Dec)

# 枚举它的所有成员
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


# 从枚举类直接派生
# unique帮我们检查保证没有重复值
@unique
class Weekday(Enum):
    """docstring for Weekday"""
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 输出枚举类
day1 = Weekday.Mon
print(day1)

print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)

print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(0))

# 报错,超出范围
# print(Weekday(7))
