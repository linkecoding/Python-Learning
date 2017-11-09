# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多进程学习
# fork()函数调用一次返回两次(子进程返回0,父进程返回子进程的ID)
import os
from multiprocessing import Process, Queue
from multiprocessing import Pool
import os
import time
import random
import subprocess
# print('Process (%s) start...' % os.getpid())
# # only works on Unix/Linux/Mac
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' %
#           (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))


# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 4)
#     end = time.time()
#     print('task %s run %0.2f secods.' % (name, (end - start)))


# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     # 生产5个子进程
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     # 不能再投入子进程
#     p.close()
#     # 让主进程等待所有的子进程执行完
#     p.join()
#     print('All subprocesses done.')

# print('$ nslookup www.python.org')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
#                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# 进程间通信

# 写数据进程执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        # 阻塞调用
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw写入
    pw.start()
    # 启动子进程pr读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程是死循环,无法将其结束,只能强行终止
    pr.terminate()
