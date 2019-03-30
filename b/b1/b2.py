# 匹配一行所有开头的字母
import re

s = "i love you but you dont love me"

# \b  一个 就近匹配
# \w  字母

content = re.findall(r'\b\w',s)
print(content)

# 匹配一行文字中所有数字开头的内容

s1= "i 11love 33you but 44you 77dont 77love 88me"

# \d  数字

content = re.findall(r'\b\d',s1)
print(content)

# 匹配 只含数字和字母的行

s2 = 'i love you \nasd51 but  \ndsa34 you dont love \n21a'
content = re.findall(r'\w+',s2,re.M)
print(content)

# 写一个正则表达式，使其能匹配‘bit’，‘bat’,'but','hat','hut'
s3 = "'bit'，'bat','but','hat','hut'"
content = re.findall(r'..t',s3)
print(content)

# 提取每行中完整的年月日和时间段
s4 = 'sw232 1987-10-10 22:44:11 asjdfhau 2018-10-20 09:12:12'

content = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',s4)
print(content)
#提取电子邮件格式
s5 = """xxxxx@gmail.com xxxxx@qq.com baidu.com 999.com"""
content =re.findall(r'\w+@\w+.com',s5)
print(content)

# 把合法的电子邮件替换成我自已的电子邮件

content =  re.sub(r'\w+@\w+.com','liuzhixin@tuling.com',s5)
print(content)

# 使用正则提取字符串中的单词

s6 = 'i love you not because who 233 of 890ssdx mot'
content = re.findall(r'\b[a-zA-Z]]',s6)
print(content)

