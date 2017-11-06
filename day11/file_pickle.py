# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import json

# python序列化(pickle)

d = dict(name='szh', age=20, score=99)
# dumps()序列化为bytes
print(pickle.dumps(d))

# dump()可以直接存储到文件
# f = open('szh.bin', 'wb')
# pickle.dump(d, f)
# f.close()


# 反序列化
f = open('szh.bin', 'rb')
d = pickle.load(f)
f.close()
print(d)

# 序列化为json
jsonstr = json.dumps(d)
print(jsonstr)
# 反序列化
print(json.loads(jsonstr))


class Student(object):
    """docstring for Student"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student('szh', 12)
# 必须将对象处理dict
s_json_str = json.dumps(s, default=lambda obj: obj.__dict__)
print(s_json_str)


def dict2stu(d):
    return Student(d['name'], d['age'])

# 兹定于对象反序列化函数
print(json.loads(s_json_str, object_hook=dict2stu))
