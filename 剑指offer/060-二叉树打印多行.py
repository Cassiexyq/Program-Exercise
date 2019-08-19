# -*- coding: utf-8 -*-

# @Author: xyq
# 层次遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        q = []
        res = []
        temp = []
        q.append(pRoot)
        while len(q):
            while len(q):
                temp.append(q.pop(0))
            val = []
            while len(temp):
                s = temp.pop(0)
                val.append(s.val)
                if s.left: q.append(s.left)
                if s.right: q.append(s.right)
            res.append(val)
        return res


s1 = TreeNode(1)
s2 = TreeNode(2)
s3 = TreeNode(3)
s4 = TreeNode(4)
s5 = TreeNode(5)
s6 = TreeNode(6)
s1.left = s2
s1.right = s3
s2.left = s4
s2.right = s5
s3.left = s6
s = Solution()
res = s.Print(s1)
print(res)



