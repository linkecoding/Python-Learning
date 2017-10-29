#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 列表生成式

list1 = list(range(1, 11))
print(list1)


list2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list2)

# 字母全排列
list3 = [m + n for m in 'ABC' for n in 'abc']
print(list3)

# 列出当前目录的所有文件夹和文件

list4 = [d for d in os.listdir('.')]
print(list4)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list5 = [key + '=' + str(value) for key, value in dict1.items()]
print(list5)


list6 = [s.upper() for s in dict1]
print(list6)