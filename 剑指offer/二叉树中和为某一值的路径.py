# -*- coding: utf-8 -*-

# @Author: xyq

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root == None: return []
        self.path.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and root.left == None and root.right == None:
            self.res.append(self.path)
        if root.left != None:
            self.FindPath(root.left, expectNumber)
        if root.right != None:
            self.FindPath(root.right,expectNumber)
        self.path = self.path[0:-1]
        return self.res