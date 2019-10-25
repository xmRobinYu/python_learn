# def my_print(args):
#     print(args)
#
#
# def move(n, a, b, c):
#     my_print((a, '-->', c)) if n == 1 else (move(n - 1, a, c, b) or move(1, a, b, c) or move(n - 1, b, a, c))
#
#
# move(3, 'a', 'b', 'c')

#
# def deduplication(nums):
#     # write your code here
#     exist_nums = set(nums)
#     return len(exist_nums)
# print(deduplication([1,1,1,1,1,1,2,7,8,2,2,2,2,2,2,2]))


#
# a=1
# str=[a]
# a=2        # 数字类型是不可变数据类型，重新开辟一块内存，把新地址与变量名绑定，并非改变原空间内的值
# print (str)


a = 444;b = 444

print(a is b)
print(a==b)