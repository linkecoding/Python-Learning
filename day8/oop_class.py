#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    """docstring for Student"""

    def __init__(self, name):
        self.name = name

    # 该方法为toString()
    def __str__(self):
        return 'Student %s' % self.name

    # 该方法为开发者调试模式下的toString()
    def __repr__(self):
        return 'Student %s' % self.name

# 斐波那契数列类


class Fib(object):
    """docstring for Fib"""

    def __init__(self):
        self.a, self.b = 0, 1

    # 返回一个可迭代对象
    def __iter__(self):
        return self

    # 每次迭代的返回值
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    # 重写该方法便可以使用下标直接访问斐波那契数列的对应位置的元素
    # 或者通过切片访问
    def __getitem__(self, n):
        # n是索引下标
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        # if isinstance(n, slice):
        #     start = n.start
        #     stop = n.stop


if __name__ == '__main__':
    # s = Student('szh')
    # print(s)
    fb = Fib()
    # for x in fb:
    #     print(x)
    print(fb[10])
