# !/usr/bin/env python3
# -×- coding: utf-8 -*-

import logging


# python异常处理
try:
    print('try...')
    r = 10 / 0
    # r = 10 / 10
    print('result = ', r)
except ZeroDivisionError as e:
    # print('except = ', e)
    logging.exception(e)
else:
    print('no exception...')
finally:
    print('finally...')
print('END')

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error')
