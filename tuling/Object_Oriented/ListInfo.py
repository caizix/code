"""
1.列表元素添加：add_key() 添加的必须是是数字或者字符串
2.列表元素取值：get_key()
3.列表合并：update_list(list)
4.删除并且返回最后一个元素：del_key()
"""
class ListInfo(object):
    def __init__(self,list_val):
        self.list = list_val
    def add_key(self,key_name):
        self.list.append(key_name)
        print(self.list)
        return "OK"

    def add_key1(self,key_name):
        if isinstance(key_name,(str,int)):
            self.list.append(key_name)
            print(self.list)
            return "OK"
        else:
            return "传入必须是字符串或者数字"
    def get_key(self,index):
        if index >=0 and index <len(self.list):
            return self.list[index]
        return "你输入太大了"
    def update_list(self,new_list):
        self.list.extend(new_list)
        return self.list
    def del_key(self):
        if len(self.list)>= 0:
            return  self.list.pop(-1)
        else:
            return "是空的"

list_info = ListInfo([1,2,3,4,5])
print(list_info.add_key1(6))
#print(list_info.get_key(5))
#print(list_info.update_list([8,9,10]))
#print(list_info.del_key())

