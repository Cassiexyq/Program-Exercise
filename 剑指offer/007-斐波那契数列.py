# -*- coding: utf-8 -*-

# @Author: xyq
# 斐波那契数列要注意哪里停止，哪里开始
class Solution:
    def Fibonacci(self,n):
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        res = 0
        n1 = 1
        n2 = 1
        for num in range(2,n):
            res = n1 + n2
            n1 = n2
            n2 = res
        return res

