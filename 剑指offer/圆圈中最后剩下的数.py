# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0: return -1
        if n == 1: return 0
        bh = range(n)
        start = 0
        while bh:
            k = (start + m -1) % n
            final = bh.pop(k)
            n -= 1
            start = k
        return final

