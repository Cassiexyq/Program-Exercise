# -*- coding: utf-8 -*-

# @Author: xyq

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.isBalanced(pRoot) != -1

    def isBalanced(self, root):
        if root == None: return 0
        left = self.isBalanced(root.left)
        if left == -1: return -1
        right = self.isBalanced(root.right)
        if right == -1: return -1
        return -1 if abs(left - right) > 1 else max(left, right)
