#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入自己编写的application函数
from wsgi_hello import application


# 创建一个服务器
httpd = make_server('', 8000, application)
print('Server HTTP on Port 8000...')
# 开始监听http请求
httpd.serve_forever()
