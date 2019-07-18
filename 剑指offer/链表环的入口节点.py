# -*- coding: utf-8 -*-

# @Author: xyq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):

        slow,fast = pHead, pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow == fast:
            fast = pHead
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow

        return None

s1 = ListNode(1)
s2 = ListNode(2)
s3 = ListNode(3)
s4 = ListNode(4)
s1.next = s2
s2.next = s3
s3.next = s2
s = Solution()
res = s.EntryNodeOfLoop(s1)
print(res.val)