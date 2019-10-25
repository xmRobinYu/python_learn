#获取能被整除的除数列表
def getmodvalue(divnum, divisorList):
    for divisor in divisorList:
        value = int(divisor)
        if value !=0 and divnum % value == 0 :
            #将能整除的除数压入堆栈
            yield value
            continue

#判断是否能被整除
def calculation(num, divisorlist):
    # 将输入的字符数组转换成int列表 ['2','3'] ->[2,3]
    divisornumlist = list(map(int, divisorlist))
    # 获取能被整除的除数列表
    result = getmodvalue(num, divisornumlist)
    a = set(iter(result))
    b = set(divisornumlist)
    #输入的除数set - 能被整除的set=不能被整除的set
    c = b - a
    #根据 a（能被整除的set）和 b（不能被整除的set）个数判断，打印的路径
    if len(a) > 0 and len(c) > 0:
        print(num, "可以被", a, "整除，不能被", c, "整除")
    elif len(a) > 0 and len(c) == 0:
        print(num, "可以被", a, "整除")
    else:
        print(num, "不能被", c, "整除")

#逻辑处理主程序
def main():
    num = int(input("请输入被除数整数(num<0时结束):\n"))
    while 1:
     if num < 0:
        print("程序结束\n")
        break
     else:
        divisorList = list(str(input("请输入除数列表(逗号分隔）:\n")).split(","))
        calculation(num, divisorList)
        num = int(input("请输入被除数整数(num<0时结束):\n"))

#main方法入口
if __name__=='__main__':
    main()
