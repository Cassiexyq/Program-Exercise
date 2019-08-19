# -*- coding: utf-8 -*-

# @Author: xyq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        i = pHead1
        j = pHead2
        while i != j:
            if i == None:
                i = pHead2
            else: i = i.next
            if j == None:
                j = pHead1
            else: j = j.next
        return i