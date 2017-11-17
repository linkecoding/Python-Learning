# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
print(base64.b64encode(b'binary'))
print(base64.urlsafe_b64encode(b'binary'))
print(base64.b64decode(b'YmluYXJ5'))
