# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件读写

# try:
#     # 以读的方式打开文件
#     f = open('test.txt', 'r')
#     # 一次性读取文件
#     content = f.read()
#     print(content)
# finally:
#     if f:
#         f.close()


# # 用with语句自动帮我们close
with open('test.txt', 'r') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        print(line.strip())


# with open('test.txt', 'r') as f:
#     for line in f.readlines():
#         # strip()把末尾的\n去掉
#         print(line.strip())

# 读取二进制流
# with open('test.png', 'rb') as f:
#     print(f.read())

# 读取特定编码的文件,遇到非法编码直接忽略
# with open('test.txt', 'r', encoding='gbk', errors='ignore') as f:
#     print(f.read())

# 写入文件,文件不存在可以自动创建
with open('test2.txt', 'w') as f:
    f.write('xiaohong')
