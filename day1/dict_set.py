# !/usr/bin/env python3
# -*- coding: utf-8 -*-

dict = {"a": 1, "b": 2, "c": 3}
print(dict)

dict['a'] = 2
dict['d'] = 123
print(dict)

print('a' in dict)
print(dict.get('v'))

dict.pop('c')
print(dict)

set1 = set([1, 2, 3])
set2 = {1, 2, 8}
x = 5
set3 = set((1, 2, 3))
print(set1)
print(set2)
