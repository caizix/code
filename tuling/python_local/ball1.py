# 有红黄蓝三种颜色的球，红3 黄3 绿6，任意摸出8个
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                print("red:{}".format(red))
                print("yellow:{}".format(yellow))
                print("green:{}".format(green))
