# -*- coding: utf-8 -*-

# @Author: xyq
# 快指针比慢指针多走k个，然后开始一起走，快指针走到头，倒数第k个结点就是慢指针
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def FindKthToTail(head, k):
    if not head:
        return None
    fast = head
    slow = head
    for _ in range(k):
        if fast:
            fast = fast.next
        else: return None
    while fast:
        fast = fast.next
        slow = slow.next
    return slow

