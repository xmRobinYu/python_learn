#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 九九乘法表
# i = 1
# while i:
#     j = 1
#     while j:
#         print(j, '*', i, '=', j * i, end = '\t\t')
#         if i == j:
#             break
#         j += 1
#         if j >= 10:
#             break
#     i += 1
#     print("\n")
#     if (i >= 10):
#         break

#
# def trim(s):
#     while s[:1] == ' ':
#         s = s[1:]
#     while s[-1:] == ' ':
#         s = s[:-1]
#     return s
#
# str = '   Ru no ob     '
# print(trim(str))

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# for num in range(10, 20):  # 迭代 10 到 20 之间的数字
#     for i in range(2, num):  # 根据因子迭代
#         if num % i == 0:  # 确定第一个因子
#             j = num / i  # 计算第二个因子
#             print('%d 等于 %d * %d' % (num, i, j))
#             break  # 跳出当前循环
#     else:  # 循环的 else 部分
#         print(num, '是一个质数')
# !/usr/bin/python
# -*- coding: UTF-8 -*-

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j):
            break
        j = j + 1
    if (j > i / j):
        print(i, " 是素数")
    i = i + 1
print("Good bye!")



