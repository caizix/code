"""
定义一个集合的操作类
1.集合元素的添加：add_serInfo()
2.集合的交集：get_intersection()
3.集合的并集：get_union()
4.集合的差集：del_difference()
"""
class SecInfo(object):
    def __init__(self,my_self):
        self.sett = my_self

    def add_setinfo(self,keyname):
        self.sett.add(keyname)
        return self.sett

    def get_intersection(self,inioninfo):
        if isinstance(inioninfo,set):
            return self.sett & inioninfo
        else:
            return "你传入的不是set"
    def get_union(self,unioninfo):
        if isinstance(unioninfo ,set):
            return self.sett | unioninfo
        else:
            return "你传入的不是set"

    def del_difference(self,unioninfo):
        return self.sett - unioninfo
S = set([1,2,3,4,5])
B = set ([5,3,4])
my_set= SecInfo(S)
#print(my_set.add_setinfo(6))
print(my_set.del_difference(B))