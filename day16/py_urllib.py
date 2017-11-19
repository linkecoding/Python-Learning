# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse

req = request.Request('http://www.douban.com/')
req.add_header(
    'User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) \
    AppleWebKit/536.26 (KHTML, like Gecko)\
     Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    data = f.read()
    print('status:', f.status, f.reason)
    for key, value in f.getheaders():
        print('%s:%s' % (key, value))
    print('Data:', data.decode('utf-8'))


print(parse.urlencode([('username', 'xiaohong'), ('username', 'xiaohong')]))
