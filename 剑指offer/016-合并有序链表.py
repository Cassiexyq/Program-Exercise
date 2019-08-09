# -*- coding: utf-8 -*-

# @Author: xyq

# 合并两个单调递增的链表，输出两个链表合并的链表


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def Merge(pHead1, pHead2):
    res = ListNode(0)
    head = res
    while pHead1 and pHead2:
        if pHead1.val <= pHead2.val:
            head.next = pHead1
            head = head.next
            pHead1 = pHead1.next
        else:
            head.next = pHead2
            head = head.next
            pHead2 = pHead2.next
    if pHead1:
        head.next = pHead1
    if pHead2:
        head.next = pHead2
    return res.next
