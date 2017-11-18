# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib

# MD5算法
md5 = hashlib.md5()
md5.update('I am'.encode('utf-8'))
md5.update(' xiaohong!'.encode('utf-8'))
print(md5.hexdigest())

# SHA1算法
sha1 = hashlib.sha1()
sha1.update('I am xiaohong!'.encode('utf-8'))
print(sha1.hexdigest())
