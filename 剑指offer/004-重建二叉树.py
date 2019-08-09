# -*- coding: utf-8 -*-

# @Author: xyq

# 根据某二叉树的前序遍历和中序遍历的结果，重建二叉树
# 假设不含重复数组

# 用前序遍历找到子数的根节点，用根节点在中序遍历种切开左右子数，递归重建二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin: return None
        root = TreeNode(pre.pop(0))  # 队列的弹出
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre,tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index+1:])
        return root


