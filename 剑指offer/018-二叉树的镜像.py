# -*- coding: utf-8 -*-

# @Author: xyq


def Mirrow(root):
    if not root: return None
    tmp = root.left
    root.left = root.right
    root.right = tmp
    Mirrow(root.left)
    Mirrow(root.right)
