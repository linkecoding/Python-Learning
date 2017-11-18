# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct

# I:四字节无符号整数   H:两字节无符号整数
print(len(struct.pack('>I', 10240099)))
print(struct.unpack('>IH', b'\x00\x9c\x00\x9c\x00\x9c'))
