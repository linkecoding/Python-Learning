# !/usr/bin/env python3
# -×- coding: utf-8 -*-

list = [1, 2, 3, 4]
print(len(list))
print(list[0])
print(list[-2])

list.append(123)
print(list)

list.pop()
list.pop(2)
print(list)
list[1] = 99;
print(list)

tuple = (1,)
print(tuple)
tuple = (1, 2, 3)
print(tuple)

tuple = (1, list)
print(tuple)
tuple[1][2] = 88
print(tuple)

age = 10
if age < 10:
	print("YES")
else:
	print("NO")


# age = input("请输入你的年龄:")
# print("年龄 = " + age)
if 12 < int(age):
	print("UUUU")

# 循环
for x in list:
	print(x)


for x in range(1, 11, 2):
	print(x)

n = 0
while n < 10:
	n += n
	print(n)
	n += 1