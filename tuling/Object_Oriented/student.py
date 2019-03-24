'''
定义一个学生类有下面属性

1.姓名

2.年龄

3.成绩（语文，数学，英语）每课成绩类型为整数类方法

4.获取学生的姓名：get_name（）返回str类型 s

5.获取学生的年纪：get_age（）返回类型int

返回3门科目中最高分，get_course()返回类型int
'''
class student(object):
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.scores)

zz = student("周周",10,[100,50,30])
print(zz.get_age())
print(zz.get_name())
print(zz.get_course())


