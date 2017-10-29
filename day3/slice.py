#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

# 切片
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = list(range(100))


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


print(list1)
print('前三个元素', list1[0:3])
print('从第二个开始取', list1[1:3])
print('倒着切片', list1[-3:-1])
print('倒着切片', list1[-3:])


print(list2)
print(list2[0:10:2])
print(list2[::5])
