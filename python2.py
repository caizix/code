APPLE = 100
a = None


def fun():
    global a
    a = 20
    return a + 100


print(APPLE)
print('a past', a)
print(fun())
print('a now', a)
