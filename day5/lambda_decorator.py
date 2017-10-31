#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

f = lambda x: x * x

print(f(12))


# def log(func):
# 	def wrapper(*args, **kw):
# 		print('call %s():' % func.__name__)
# 		return func(*args, **kw)
# 	return wrapper


def log(*text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			if len(text) == 0:
				print('call %s():' % (func.__name__))
			else:
				print('text = %s, call %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator


@log('abc', 'fe')
def now(a, b):
	return '2017-10-31'


print(now(1, 2))
print(now.__name__)