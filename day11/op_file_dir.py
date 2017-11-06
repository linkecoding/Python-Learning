# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 如果是posix，
# 说明系统是Linux、Unix或Mac OS X，
# 如果是nt，就是Windows系统。
print(os.name)

# 更详细的系统信息
print(os.uname())

# 查看环境变量
print(os.environ)

# 获取具体的某个环境变量
print(os.environ.get('path'))


# 操作目录
print(os.path.abspath('.'))
# 先表示出要创建目录的完整路径
idir = os.path.join(os.path.abspath('.'), 'dir')
# 创建目录
# print(os.mkdir(idir))
# 删除目录
# print(os.rmdir(idir))
# 注意:使用join可以保证使用基于系统的正确的文件分隔符


# 拆分目录
idir = os.path.join(idir, '1.txt')
print(os.path.split(idir))

# 拆分出文件扩展名
print(os.path.splitext(idir))

# 对文件重命名
os.rename('test.txt', 'test.txt')

# 删除文件
# os.remove('test2.txt')

# 复制文件
import shutil
shutil.copyfile('test.txt', 'test2.txt')

# 列出当前目录的所有文件夹
dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
print('------------------------------')
print(dirs)

# 列出当前目录的所有py文件
files = [x for x in os.listdir('.') if os.path.isfile(
    x) and os.path.splitext(x)[1] == '.py']
print('------------------------------')
print(files)
