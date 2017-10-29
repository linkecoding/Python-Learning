#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

list1 = [1, 2, 3, 4, 5, 6, 7]
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(dict1)

for key in dict1:
	print(key)


for value in dict1.values():
	print(value)

for key, value in dict1.items():
	print(key, '--->', value)

print(isinstance('abc', Iterable))

for i, value in enumerate(list1):
	print(i, '--->', value)

for y in list1:
	print('-->', y)