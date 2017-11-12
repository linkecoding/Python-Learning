# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

strs = "python"
if re.match(r'\w\d*', strs):
    print('OK')
else:
    print('Fail')


# 切分字符串
strs = 'a b  c'
print(strs.split(' '))
print(re.split(r'\s+', strs))

strs = 'a,b; c;  d '.strip()
print(re.split(r'[\s\,\;]+', strs))


# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 编译正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-123456').groups())
