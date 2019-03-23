# 判断年份是否是闰年
year = input("请输入年份：")
# 判断用户输入的是不是数字
while (1):
    year = input("请输入年份：")
    if year.isdigit():
        year = int(year)

        if year % 4 == 0:
            print(str(year) + "是润年")
        else:
            print(str(year) + "不是闰年")
    else:
        print("叫你输入年份!!!!!")
