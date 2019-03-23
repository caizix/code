# print("hello world!")
# print("TuLing"*5)
# print('hahah""')
# print("\"")

# print("我就是想打印一个双引号\"")


# 编写程序，要求用户输入姓名并且打印“你好，姓名”
# name=input("请输入姓名：")
# print("你好，"+name)

# 编写程序，要求用户输入1-100之间的整数并且判断，输入符合要求的打印“你好看”，否则的打印“你丑八怪，天黑别把灯打开”
temp = input("请输出1个整数：")
if temp.isdigit():
    temp = int(temp)
    if 1 <= temp <= 100:
        print("你好看")
    else:
        print("丑八怪，天黑别把灯打开")
else:
    print("丑八怪，天黑别把灯打开")
