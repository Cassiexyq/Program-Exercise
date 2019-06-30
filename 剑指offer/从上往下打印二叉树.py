# -*- coding: utf-8 -*-

# @Author: xyq

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root :
            return []
        queue = [root]
        res = []
        while queue:
            n = queue.pop(0)
            res.append(n.val)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        return res

