# -*- coding: utf-8 -*-

# @Author: xyq
# 中序遍历
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
        if pNode.right:  # 右子树不为空，找右子树的最左结点
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        if not pNode.right: # 右子树为空，找父节点，知道父节点的左子树是当前的哪个结点
            while pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                pNode = pNode.next
        return None
