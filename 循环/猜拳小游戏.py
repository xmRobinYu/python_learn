import random

while 1:
    a = int(random.uniform(1, 4))
    if a == 1:
        randomValue = '石头'
    elif a == 2:
        randomValue = '剪刀'
    else:
        randomValue = '布'
    inputValue = input('输入 石头、剪刀、布,输入"end"结束游戏:\n')
    list = ['石头', '剪刀', '布']
    if inputValue not in list and inputValue != 'end':
        print("输入错误，请重新输入：\n")
    elif inputValue == 'end':
        print("游戏结果！")
        break
    elif inputValue == randomValue:
        print("电脑出 " + randomValue + "  平局")
    else:
        index = 1
        randomValueIndex = 1
        mIndex = 1
        for value in list:
            if (value == randomValue):
                randomValueIndex = index
            elif (value == inputValue):
                mIndex = index
            index += 1
        if ((randomValueIndex == 1 and mIndex == len(list)) or (randomValueIndex == len(list) and mIndex == 1)):
            if (randomValueIndex > mIndex):
                print("电脑出 " + randomValue + "  电脑赢了")
            else:
                print("电脑出 " + randomValue + "  电脑输了")
        else:
            if (randomValueIndex < mIndex):
                print("电脑出 " + randomValue + "  电脑赢了")
            else:
                print("电脑出 " + randomValue + "  电脑输了")


