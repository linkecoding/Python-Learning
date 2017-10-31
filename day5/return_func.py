#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum


f = lazy_sum(*[1, 2, 3, 4])

print(f)
print(f())