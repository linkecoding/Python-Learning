#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fn(self, name='world'):
    print('Hello, %s' % name)


# 通过type函数创建出Hello类
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()
