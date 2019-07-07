# -*- coding: utf-8 -*-

# @Author: xyq
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None: return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))

