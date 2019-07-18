# -*- coding: utf-8 -*-

# @Author: xyq



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot: return []
        queue = []
        res = []
        temp = []
        queue.append(pRoot)
        layer = 1
        while len(queue) != 0:
            v = []
            while len(queue) != 0:
                temp.append(queue.pop(0))
            while len(temp) != 0:
                temp_val = temp.pop(0)
                if temp_val.left:
                    queue.append(temp_val.left)
                if temp_val.right:
                    queue.append(temp_val.right)
                v.append(temp_val.val)
            if layer % 2 == 1:
                res.append(v)
            else: res.append(list(reversed(v)))
            layer += 1

        return res
    def stackprint(self, pRoot):
        if not pRoot: return None
        stack1 = []
        stack2 = []
        res = []

        stack1.append(pRoot)
        while len(stack1) != 0 or len(stack2) != 0:
            if len(stack1) != 0:
                val = []
                while len(stack1) !=0 and len(stack2) == 0:
                    temp = stack1.pop(-1)
                    val.append(temp.val)
                    if temp.left: stack2.append(temp.left)
                    if temp.right: stack2.append(temp.right)
                print(val)
                res.append(val)
            if len(stack2) !=0 and len(stack1) == 0:
                val = []
                while len(stack2) != 0:
                    temp = stack2.pop(-1)
                    val.append(temp.val)
                    if temp.right: stack1.append(temp.right)
                    if temp.left: stack1.append(temp.left)
                print(val)
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
res = s.stackprint(s1)
print(res)

