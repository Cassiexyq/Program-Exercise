# -*- coding: utf-8 -*-

# @Author: xyq

"""
Definition of ListNode
 链表长度每增长2，后移一位
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if not head or not head.next or not head.next.next: return head
        pre = head
        cur = head.next.next
        while cur.next and cur.next.next:
            pre = pre.next
            cur = cur.next.next
        return pre.next


