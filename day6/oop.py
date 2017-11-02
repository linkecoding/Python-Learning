#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    """docstring for Student"""

    def __init__(self, name, age):
        super(Student, self).__init__()
        self.__name = name
        self.__age = age


class Animal(object):
    """docstring for Animal"""

    def run(self):
        print('Animal is running')


class Dog(Animal):
    """docstring for Dog"""

    def run(self):
        print('Dog is running')


class Cat(Animal):
    """docstring for Cat"""

    def run(self):
        print('Cat is running')


def test(animal):
    animal.run()

if __name__ == '__main__':
    animal = Animal()
    cat = Cat()
    dog = Dog()
    test(animal)
    test(cat)
    test(dog)

    student = Student()
