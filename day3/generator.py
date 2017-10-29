#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器

g = (x * x for x in range(1, 11))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for x in g:
# 	print(x)


def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'

# fib(12)


def fib2(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

g = fib2(10) 
while True:
	try:
		x = next(g)
		print(x)
	except Exception as e:
		print(e.value)
		break
