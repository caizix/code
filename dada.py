class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        a = pHead
        b = pHead.next
        a.next = None
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        return a
