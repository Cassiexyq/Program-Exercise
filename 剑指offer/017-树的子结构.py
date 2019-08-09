# -*- coding: utf-8 -*-

# @Author: xyq
# 判断B是不是A的子结构，遍历父节构，判断子结构是否相同
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def HasSubtree(pRoot1, pRoot2):
    if not pRoot1 or not pRoot2: return False
    return isSubtree(pRoot1, pRoot2) or isSubtree(pRoot1.left, pRoot2) or isSubtree(pRoot1.right, pRoot2)

def isSubtree(left, right):
    if not right: return True
    if not left: return False
    if left.val != right.val: return False
    else:
        return isSubtree(left.left, right.left) and isSubtree(left.right, right.right)

