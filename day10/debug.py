# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdb
# import logging
# logging.basicConfig(level=logging.DEBUG)
# # python调试


# def foo(s):
#     n = int(s)
#     logging.info('n = %d' % n)
#     return 10 / 0


# def main():
#     foo('0')

# main()

s = '0'
n = int(s)
# 设置了一个断点
pdb.set_trace()

print(10 / n)
