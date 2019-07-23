# -*- coding: utf-8 -*-

# @Author: xyq

# 二叉搜索树 中序遍历 从小到大，遍历到第k个值的就是第k小的结点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot: return None
        stack = []
        index = 0
        while pRoot or len(stack) != 0:
            while pRoot:
                stack.append(pRoot)
                pRoot = pRoot.left
            pRoot = stack.pop(-1)
            index += 1
            if index == k:
                return pRoot
            pRoot = pRoot.right
