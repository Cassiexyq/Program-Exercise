# -*- coding: utf-8 -*-

# @Author: xyq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead == None or pHead.next == None:
            return None
        slow = pHead
        fast = pHead
        while slow != None and slow.next != None:
            slow = slow.next
            fast = slow.next.next
            if slow == fast:
                fast = pHead
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                if slow == fast:
                    return slow

        return None