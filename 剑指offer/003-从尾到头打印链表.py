# -*- coding: utf-8 -*-

# @Author: xyq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# 解法1 ： 用辅助栈存储
def printListFromTailToHead(listNode):
    stack = []
    res = []
    node = listNode
    while node:
        stack.append(node.val)
        node = node.next
    while stack:
        res.append(stack.pop(-1))
    return res
# 解法2：本身栈调用
def printListFromTailToHead2(listNode):
    if listNode:
        return printListFromTailToHead2(listNode.next) + [listNode.val]
    else:
        return []
res = []
def solution3(listNode):
    if listNode:
        solution3(listNode.next)
        res.append(listNode.val)
    return res


