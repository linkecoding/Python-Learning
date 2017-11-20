# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import chardet

data = '我是谁'.encode('utf-8')
print(chardet.detect(data))
