# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import hmac
message = b'Hello World!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())
