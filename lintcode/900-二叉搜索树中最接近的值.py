# -*- coding: utf-8 -*-

# @Author: xyq



"""
Definition of TreeNode:
递归判断这棵树，如果当前结点值小于目标值，只可能是当前结点值或右子树的值，如果当前结点值大于目标值，只可能是当前结点值或左子树的值
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if root.val == target:
            return root.val
        if root.val < target:
            if not root.right: return root.val
            right = self.closestValue(root.right, target)
            if abs(root.val-target) <= abs(right-target): return root.val
            return right
        else:
            if not root.left: return root.val
            left = self.closestValue(root.left, target)
            if abs(root.val - target) <= abs(left-target): return root.val
            return left
