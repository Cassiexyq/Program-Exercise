# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    def Sum_Solution(self, n):
        res = n
        b = res and self.Sum_Solution(n-1)
        res += b
        return res

