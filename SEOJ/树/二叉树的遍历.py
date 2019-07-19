# -*- coding: utf-8 -*-

# @Author: xyq



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.res1 = []
        self.res2 = []
        self.res3 = []
    # 递归
    def xianxu(self,pRoot):
        if not pRoot: return
        self.res1.append(pRoot.val)
        self.xianxu(pRoot.left)
        self.xianxu(pRoot.right)
    def zhongxu(self,pRoot):
        if not pRoot: return
        self.zhongxu(pRoot.left)
        self.res2.append(pRoot.val)
        self.zhongxu(pRoot.right)
    def houxu(self, pRoot):
        if not pRoot: return
        self.houxu(pRoot.left)
        self.houxu(pRoot.right)
        self.res3.append(pRoot.val)
    # 非递归
    def xianxu2(self,pRoot):
        if not pRoot: return
        stack = []
        res = []
        while pRoot or len(stack) != 0:
            while pRoot:
                res.append(pRoot.val)
                stack.append(pRoot)
                pRoot = pRoot.left
            pRoot = stack.pop(-1)
            pRoot = pRoot.right
        return res
    def zhongxu2(self,pRoot):
        if not pRoot: return
        res = []
        stack = []
        while pRoot or len(stack) != 0:
            while pRoot:
                stack.append(pRoot)
                pRoot = pRoot.left
            pRoot = stack.pop(-1)
            res.append(pRoot.val)
            pRoot = pRoot.right
        return res
    def houxun2(self,pRoot):
        if not pRoot: return
        reserv = []
        res = []
        stack = []
        while pRoot or len(stack) != 0:
            while pRoot:
                reserv.append(pRoot.val)
                stack.append(pRoot)
                pRoot = pRoot.right
            pRoot = stack.pop(-1)
            pRoot = pRoot.left
        while reserv:
            res.append(reserv.pop(-1))
        return res


s1 = TreeNode(4)
s2 = TreeNode(2)
s3 = TreeNode(6)
s4 = TreeNode(1)
s5 = TreeNode(3)
s6 = TreeNode(5)
s7 = TreeNode(7)
s1.left = s2
s1.right = s3
s2.left = s4
s2.right = s5
s3.left = s6
s3.right = s7
s = Solution()
s.xianxu(s1)
print(s.res1)
print(s.xianxu2(s1))
s.zhongxu(s1)
print(s.res2)
print(s.zhongxu2(s1))
s.houxu(s1)
print(s.res3)
print(s.houxun2(s1))
