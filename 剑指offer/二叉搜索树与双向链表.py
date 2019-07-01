# -*- coding: utf-8 -*-

# @Author: xyq

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.head = None
        self.res = None
    def Convert(self, pRootOfTree):
        if not pRootOfTree: return None
        self.Convert(pRootOfTree.left)
        # 第一次运行链表，它会使最左边叶子节点为链表第一个节点
        if not self.res:
            self.head = pRootOfTree
            self.res = pRootOfTree
        else:
            # 把根节点插入到双向链表右边，rightHead向后移动
            self.res.right = pRootOfTree
            pRootOfTree.left = self.res
            self.res = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.head

