# -*- coding: utf-8 -*-

# @Author: xyq
# 1 2 3 4 5
# 1 p
# 2 q
# 2-1
# 3-2-1
# 4-3-2-1
# 5-4-3-2-1

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseList(pHead):
    q = pHead.next
    p = pHead
    p.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r
    return p


