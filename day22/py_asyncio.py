#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio


@asyncio.coroutine
def hello():
    print('Hello, World!')
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(10)
    print('Hello again!')


# 获取EventLoop
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
