# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from contextlib import contextmanager, closing
from urllib.request import urlopen


class Query(object):
    """docstring for Query"""

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info %s...' % self.name)


class Qu(object):
    """docstring for Qu"""

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Qu(name)
    yield q
    print('End')


with Query('Bob') as q:
    q.query()


with create_query('Bob') as q:
    q.query()


with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(str(line).strip())
