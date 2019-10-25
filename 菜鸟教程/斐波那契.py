#!/usr/bin/python3
import sys

#
# def fibonacci(n):  # 生成函数--斐波那契
#     a, b, conter = 1, 1, 0
#     while True:
#         if (conter > n):
#             return
#         # yield a
#         a, b = b, a + b
#         print('%d,%d' % (a, b))
#         conter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
# # for x in f:
# #     print(x,end=' ')
#
# # while True:
# #     try:
# #         print(next(f), end=' ')
# #     except StopIteration:
# #         sys.exit()
# def get():
#     m = 0
#     n = 2
#     l = ['s', 1, 3]
#     k = {1: 1, 2: 2}
#     p = ('2', 's', 't')
#     while True:
#         m += 1
#         yield m
#         yield m, n, l, k, p
#
#
# it = get()
# print(next(it))  # 1
# print(next(it))  # (1, 2, ['s', 1, 3], {1: 1, 2: 2}, ('2', 's', 't'))
#
# print(next(it))  # 2
# print(type(next(it)))  # <class 'tuple'>
#
# print(next(it))  # 1
# print(next(it))  # (1, 2, ['s', 1, 3], {1: 1, 2: 2}, ('2', 's', 't'))

def myYield_1():
    a, i = 'yield', 0
    while True:
        print('before #%d' % i, end=", ")
        yield a, i
        print('after #%d' % i, end=", ")
        i += 1

def myYield_2():
    a, i = 'yield_a', 0
    b, i = 'yield_b', 0
    while True:
        print('before #%d' % i, end=", ")
        yield a, i
        yield b, i
        print('after #%d' % i, end=", ")
        i += 1

it1 = iter(myYield_1())
it2 = iter(myYield_2())

for i in range(10):
    print("next #%d" % i, end=": ")
    print(next(it1))
print('\n')
for i in range(10):
    print("next #%d" % i, end=": ")
    print(next(it2))