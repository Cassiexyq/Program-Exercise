# -*- coding: utf-8 -*-

# @Author: xyq

def rectCover(n):
    if n == 0: return -1
    if n == 1: return 1
    if n == 2: return 2
    n1 = 1
    n2 = 1
    res = 0
    for _ in range(3,n+1):
        res = n1 + n2
        n1 = n2
        n2 = res
    return res


