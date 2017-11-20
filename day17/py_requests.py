# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# r = requests.get('https://www.douban.com/')
# print(r.status_code)
# print(r.text)


r2 = requests.get('https://www.douban.com/search',
                  params={'q': 'python3', 'cat': '1001'})
print(r2.url)
print(r2.status_code)
print(r2.text)
print(r2.encoding)
print(r2.content)

url = 'https://www.douban.com/search'
requests.get(url, params={'a': '1'})

requests.get(url, headers={})
requests.get(url, cookies={})
requests.get(url, timeout=2.5)

requests.post(url, data={})

requests.post(url, json={})

requests.post(url, files={'file': open('test.png', 'rb')})

print(r2.headers)

print(r2.cookies)
