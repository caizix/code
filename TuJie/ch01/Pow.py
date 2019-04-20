def Pow(x,y):
    p = 1
    for i in range (1,y+1):
        p *= x
    return p
print(Pow(4,3))