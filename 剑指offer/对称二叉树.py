# -*- coding: utf-8 -*-

# @Author: xyq
# 递归和非递归  左子树的左子树和右子树的右子树一样，左子树的右子树和右子树的左子树一样
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot: return True
        return self.checkzx(pRoot.left, pRoot.right)
    # 递归遍历左右结点
    def checkzx(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            if self.checkzx(pRoot1.left, pRoot2.right) and self.checkzx(pRoot1.right, pRoot2.left):
                return True
        return False
    def dfs(self, pRoot):
        if not pRoot: return True
        a = []
        a.append(pRoot.left)
        a.append(pRoot.right)
        while len(a) != 0:
            temp1 = a.pop(-1)
            temp2 = a.pop(-1)
            if not temp1 and not temp2:
                continue
            if not temp1 or not temp2:
                return False
            if temp1.val != temp2.val:
                return False
            a.append(temp1.left)
            a.append(temp2.right)
            a.append(temp1.right)
            a.append(temp2.left)
        return True

