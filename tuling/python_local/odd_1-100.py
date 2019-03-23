# 写出一个程序打印出所有的奇数
# ls=range(1,101)
# for i in ls:
#    if i%2==1:
#        print(i)



# 有一个长阶梯，若每步上2阶，剩1阶，上3阶剩2阶，上5阶，剩4阶，上6阶剩5.上7不剩
x = 0
while x < 1000:
    if (x % 2 == 1) \
            and (x % 3 == 2) \
            and (x % 5 == 4) \
            and (x % 6 == 5) \
            and (x % 7 == 0):
        print(x)
        x += 1
    else:
        x += 1
print("循环结束")
