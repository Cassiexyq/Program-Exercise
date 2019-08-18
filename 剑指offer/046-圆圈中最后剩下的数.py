# -*- coding: utf-8 -*-

# @Author: xyq
# 约瑟夫环： 数组，链表，递归
# 编号从0-n-1  和 1-n
class Solution:
    def f(self,n,m):
        if n == 1: return n
        return (self.f(n-1,m) + m-1) % n+1 # 从1开始报数,编号从1，2开始
        # if n == 0: return n
        # return (self.f(n-1,m) + m) % n # 从0开始报数，编号从0
    def LastRemaining_Solution(self, n, m): # 编号0开始，报数从0开始
        if n == 0: return -1
        if n == 1: return 0
        bh = [i for i in range(n)]
        start = 0
        while bh:
            k = (start + m -1) % n
            final = bh.pop(k)
            n -= 1
            start = k
        return final

s = Solution()
print(s.f(10,3))
print(s.LastRemaining_Solution(10,3))