#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(sorted([0, -2, 9, 4, 7]))

# 传入处理函数
print(sorted([0, -2, 9, 4, 7], key = abs))

# 字符串ASCII排序
print(sorted(['bob', 'moer', 'Zoo', 'Credit']))
# 忽略大小写排序
print(sorted(['bob', 'moer', 'Zoo', 'Credit'], key = str.lower))

# 逆序
print(sorted(['bob', 'moer', 'Zoo', 'Credit'], key = str.lower, reverse = True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0].lower()


def by_score(t):
	return t[1]



L2 = sorted(L, key=by_name)

L3 = sorted(L, key = by_score)
print(L2)
print(L3)