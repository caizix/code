# 给用户三次机会，猜想我们程序生产的一个数字A，每次用户猜想过后会提示数字是否正确以及用户输入数字是大于还是小于A，当机会用尽提示用户已经输掉游戏
import random

# 计算机生成的随机数
secret = random.randint(1, 100)
# 初始化用户的次数
times = 3
while times:
    num = input("请输入数字：")
    if num.isdigit():
        temp = int(num)
        if temp == secret:
            print("你输入对了")
            break
        elif temp < secret:
            print("你输入小了!!!")
            times = times - 1
        else:
            print("你输入大了!!!!")
            times = times - 1
    else:
        print("叫你输入数字！！！")

print("你没有机会了！！！！！！！！！！")
