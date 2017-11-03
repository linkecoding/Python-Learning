#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多继承,可以对各种功能进行组合,添加额外功能


# 动物类
class Animal(object):
    """docstring for Animal"""

    def __init__(self, arg):
        super(Animal, self).__init__()
        self.arg = arg


# 哺乳动物
class Mammal(Animal):
    """docstring for Mammal"""

    def __init__(self, arg):
        super(Mammal, self).__init__()
        self.arg = arg


# 鸟类
class Bird(Animal):
    """docstring for Bird"""

    def __init__(self, arg):
        super(Bird, self).__init__()
        self.arg = arg


# 能跑的
class Runnable(object):
    """docstring for Runnable"""

    def __init__(self, arg):
        super(Runnable, self).__init__()
        self.arg = arg

    def run(self):
        print('Running...')


# 能飞的
class Flyable(object):
    """docstring for Flyable"""

    def __init__(self, arg):
        super(Flyable, self).__init__()
        self.arg = arg

    def fly(self):
        print('Flying...')


# 各种动物
# 狗 哺乳动物
class Dog(Mammal, Runnable):
    """docstring for Dog"""

    def __init__(self, arg):
        super(Dog, self).__init__()
        self.arg = arg


# 蝙蝠 哺乳动物
class Bat(Mammal, Flyable):
    """docstring for Bat"""

    def __init__(self, arg):
        super(Bat, self).__init__()
        self.arg = arg


# 鹦鹉
class Parrot(Bird, Flyable):
    """docstring for Parrot"""

    def __init__(self, arg):
        super(Parrot, self).__init__()
        self.arg = arg


# 鸵鸟
class Ostrich(Bird, Runnable):
    """docstring for Ostrich"""

    def __init__(self, arg):
        super(Ostrich, self).__init__()
        self.arg = arg
