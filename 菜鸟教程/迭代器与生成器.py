import sys  # 引入 sys 模块

# list = [1, 2, 3, 4]
# it = iter(list)
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
