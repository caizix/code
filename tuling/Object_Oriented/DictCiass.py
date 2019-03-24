"""
1.删除某个key_del_dict(key)
2.判断某个键是否在字典里，如果返回键对值，不在则返回
3.返回键组成的列表，返回类型：list get_key()
4.合并字典，并且返回合并后字典的values组成的列表，返回类型list update_dict()
"""
class DictClass(object):
    def __init__(self,dict):
        self.dict = dict
    def del_dict(self,key):
        if key not in self.dict.key():
            return "key不在字典中"
        else:
            self.dict.pop(key)
            return "删除成功"
    def get_dict(self,key):
        if key not in self.dict.key:
            return "not found"
        else:
            return self.dict[key]
    def get_key(self):
        return self.dict.keys()

    def update_dict(self,dict2):
        self.dict = dict(self.dict,**dict2)
        return self.dict.values()