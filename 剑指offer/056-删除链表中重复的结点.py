# -*- coding: utf-8 -*-

# @Author: xyq

# 排序的链表，存在重复结点，去掉重复点
# 1-2-3-3-4-4-5  -》   1-2-5
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        if pHead.val == pHead.next.val:
            res = pHead.next
            while res and res.val == pHead.val:
                res = res.next
            return self.deleteDuplication(res)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead
    def delete2(self, pHead):
        head = ListNode(0)
        q = pHead
        p = head
        while q:
            while q and q.next and q.next.val == q.val:  # 出现多个数的连续重复
                temp = q.val
                while q and q.val == temp:
                    q = q.next
            if q:
                p.next = q
                p = p.next
                q = q.next
            else:
                p.next = q

        return head.next

s1 = ListNode(1)
s2 = ListNode(2)
s3 = ListNode(3)
s4 = ListNode(3)
s5 = ListNode(3)
s1.next = s2
s2.next = s3
s3.next = s4
s4.next = s5
s5.next = None
s = Solution()

res = s.delete2(s1)
while res:
    print(res.val)
    res = res.next