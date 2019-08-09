# -*- coding: utf-8 -*-

# @Author: xyq

def floor(n):
    if n == 1: return 1
    res = 1
    for _ in range(n-1):
        res = 2 * res
    return res

