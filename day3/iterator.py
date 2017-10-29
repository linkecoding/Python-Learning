#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterator

list1 = [1, 2, 3, 4]
print(isinstance(list1, Iterator))
print(isinstance(iter(list1), Iterator))