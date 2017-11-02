#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __slots__限制了只能动态给类和实例添加的属性
from types import MethodType


class Student(object):
    """docstring for Student"""
    # __slots__ = ('name', 'age')


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


# 给一个实例绑定一个方法
s = Student()
s.set_age = MethodType(set_age, s)
s.set_age(12)
print(s.age)

# 给一个class绑定方法
Student.set_score = set_score
s.set_score(100)
print(s.score)
