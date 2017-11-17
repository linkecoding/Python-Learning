# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

# deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
