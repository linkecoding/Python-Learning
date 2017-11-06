# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from io import BytesIO
# StringIO  在内存中读写str

# 首先创建StringIO,然后写入,
# 最后通过getvalue()获得写入的str

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())


# 读取StringIO, 可以用str初始化一个StringIO,然后读取
f = StringIO('hello \n world!')
while True:
    line = f.readline()
    if line == '':
        break
    print(line.strip())


# ByteIO 可以在内存中操作bytes
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
