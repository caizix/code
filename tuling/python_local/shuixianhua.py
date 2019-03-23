# 求100-999以内的水仙花数153=1^3+5^3+3^3
for i in range(100, 1000):
    temp = list(str(i))
    a = temp[0]
    b = temp[1]
    c = temp[2]
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
