# -*- coding: utf-8 -*-

# @Author: xyq

"""
Definition of TreeNode:
加一个层数标签
"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        q = deque()
        if not root: return []
        q.append(root)
        res = []
        level = 0
        while q:
            res.append([])
            for i in range(len(q)):
                node = q.popleft()
                res[level].append(node.val)
                if node.left and node.left.val != '#':
                    q.append(node.left)
                if node.right and node.right.val != '#':
                    q.append(node.right)
            level += 1
        return res









