#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

# map函数
def f(x):
	return x * x

r = map(f, [1, 2, 3, 4, 5, 6])
print(list(r))

def f2(x, y):
	return x + y


print(reduce(f2, [1, 2, 3, 4]))

def f3(x, y):
	return x * 10 + y


print(reduce(f3, [1, 2, 3, 4]))

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}[s]
	return reduce(fn, map(char2num, s))

print(str2int('1234'))
print({'1': 1, '2': 2, '3': 3}['1'])

dict1 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}
print(dict1['1'])

def normalize(name):
	return name[0].upper() + name[1:].lower()

l1 = ['adam', 'LISA', 'barT'];
print(list(map(normalize, l1)))

l2 = [1, 2, 3, 4, 5, 6]
def prod(x, y):
	return x * y

print(reduce(prod, l2))

def str2float(s):
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}[s]

	def f(x, y):
		return x * 10 + y

	i = s.index('.')
	bef = s[:i]
	lat = s[i+1:]
	befn = reduce(f, map(char2num, bef))
	latn = reduce(f, map(char2num, lat))
	return befn + latn / (10 ** len(lat))



print(str2float('111112.12221200'))