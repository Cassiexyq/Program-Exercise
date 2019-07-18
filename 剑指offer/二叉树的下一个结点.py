# -*- coding: utf-8 -*-

# @Author: xyq

# 有右子树就找右子树的最左结点
# 没有右子树 ， 如果是其父节点的左子树，父节点就是下一个结点
#               如果是父节点的右子树，找到父节点的父节点直到父节点没有父节点的那个父节点
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode: return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        if not pNode.right:
            while pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                pNode = pNode.next
        return None
