#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a, b = (1, 2)
print(a)
print(b)


# 定义普通函数
def func1(a, b):
    return a * b


# 定义有默认值的函数
def func2(a, b=2):
    return a * b


# 定义可变参数的函数(多次调用存在问题)
# 因为此处的默认参数也是一个变量,每次添加后返回的都是被改变的值,所以默认参数必须被指向不可变参数
def func21(L=[]):
    L.append('End')
    return L


def func22(L=None):
    if L is None:
        L = []
    L.append('End')
    return L


# 可变参数(内部其实为tuple)
def func3(*nums):
    sum = 0
    for x in nums:
        sum = sum + x
    return sum


# 关键字参数(传入的是key-value对)
def func4(name, age, **kw):
    return {'name': name, 'age': age, 'others': kw}


# 命名关键字参数(规定了key值的关键字参数)
# 一般参数和命名关键字参数之间要使用*隔开
# 如果前面已经存在可变参数,则不需要*
def func5(name, age, *, job, city):
    print(name, age, job, city)


def func51(name, age, *info, city):
    print(info, city)

# 如何前面有可变参数,则不能再出现*分割隔
# def func52(name, age, *info, *, city):
#     print(info, city)


print(func1(a, b))
print(func2(4))
print(func21())
print(func21())
print(func22())
print(func22())
print(func3(1, 2, 3))
a = (1, 3, 4)
b = [1, 2, 4, 8]
# 必须在前面加*
print(func3(*a))
print(func3(*b))

# 传入key-value
print(func4('szh', 21, home='city'))

maps = {'home': 'city', 'say': 'hello'}
# 必须在前面加**
print(func4('szh', 21, **maps))

print(func5('szh', 12, job='android', city='sh'))
print(func51('szh', 12, 'haha', city='sh'))
print(func52('szh', 12, 'haha', city='sh'))
