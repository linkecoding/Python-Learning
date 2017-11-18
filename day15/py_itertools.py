# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

# natuals = itertools.count(1)
# for x in natuals:
#     print(x)

# cs = itertools.cycle("ABC")
# for x in cs:
#     print(x)


# ns = itertools.repeat('ABC', 5)
# for x in ns:
#     print(x)

# na = itertools.count(1)
# ns = itertools.takewhile(lambda x: x < 10, na)
# print(list(ns))


# for x in itertools.chain('ABC', 'XYZ'):
#     print(x, end='')

# 将相邻的重复元素放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
