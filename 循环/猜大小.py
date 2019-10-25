import random

s = int(random.uniform(1, 100))
print(s)
m = int(input('请输入整数：\n'))
while m != s:
    if m > s:
        print("大了")
        m = int(input('请输入整数：\n'))
    if m < s:
        print("小了")
        m = int(input('请输入整数:\n'))
    if m == s:
        print("猜对了")
