"""
1.门票原价是100元
2.当周末时候门票涨20%
3.小孩子半价
4.计算2个成人和1个小孩子平日票价
"""

class Ticket():
    def __init__(self,weekend=False,child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1
    def cal_price(self,num):
        return self.exp * self.inc * self.discount * num
adult = Ticket()
child = Ticket(child=True)


print("两个成年人和一个小孩子平常价格是{}".format(adult.cal_price(2)+child.cal_price(1)))