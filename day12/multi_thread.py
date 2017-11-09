# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多线程学习

# threading 是对低级模块 _thread的封装
import time
import threading

# 新线程执行的代码
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)


# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


balance = 0
# 生成一把锁
lock = threading.Lock()


def change_it(n):
    # 先存后取,结果应该为0
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        # 获得锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
