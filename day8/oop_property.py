#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @property可以以方法的形式定义一个属性
# @score.setter可以为该属性定义一个get方法
# 这样简化了set和get函数
# 同事可以自定义一些只读属性或者可读写属性


class Student(object):
    """docstring for Student"""
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# s = Student()
# s.set_score(40)
# print(s.get_score())

s2 = Student()
s2.score = 10
print(s2.score)
