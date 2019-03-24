"""
定义一个乌龟类和鱼类
1.假设游戏场景为范围（x，y）为0<=x<=10,0<=y<=10
2.游戏生成一只乌龟和10条鱼
3.他们的移动方式均是随机的
4.乌龟的最大移动能力是2（可以随机选择1或者2），鱼的最大移动能力是1
5.当移动到边缘时候，自动反向方向移动
6.乌龟的上线体力为100
7.乌龟每移动1次，体力消耗1
8.当乌龟和鱼重叠，乌龟吃掉鱼，体力增加20
9.鱼不计算体力
10.当乌龟体力值为0或者鱼的数量为0，游戏结束
"""
import random as r
class Tutle(object):
    def __init__(self):
        self.power = 100

        #初始化乌龟的位置
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        new_x = r.choice([1,2,-1,-2])+self.x
        new_y = r.choice([1,2,-1,-2])+self.y
        # 判断是否超出边界
        if new_x < 0:
            self.x = 0-(new_x - 0)
        elif new_x > 10:
            self.x = 10 -(new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0-(new_y - 0)
        elif new_y > 10:
            self.y = 10 -(new_y - 10)
        else:
            self.y = new_y

        self.power -= 1
        return (self.x,self.y)
    def eat(self):
        self.power += 20
        if self.power >= 100:
            self.power = 100
class Fish(object):
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        new_x = self.x + r.choice([1,-1])
        new_y = self.y + r.choice([1,-1])
        if new_x < 0:
            self.x = 0-(new_x - 0)
        elif new_x > 10:
            self.x = 10 -(new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0-(new_y - 0)
        elif new_y > 10:
            self.y = 10 -(new_y - 10)
        else:
            self.y = new_y
        return (self.x,self.y)


turtle = Tutle()
fish = []
for i in range (10):
    new_fish = Fish()
    fish.append(new_fish)
while True:
    if not len(fish):
        print("鱼被吃完了")
        break
    if not turtle.power:
        print("乌龟体力耗尽了")
        break

    pos =turtle.move()
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼被吃掉了")