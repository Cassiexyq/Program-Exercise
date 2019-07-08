# -*- coding: utf-8 -*-

# @Author: xyq
class Solution:
    def LeftRotateString(self, s, n):
        j = len(s)
        if j == 0: return ""
        if n == 0: return s
        n %= j
        return s[n:] + s[:n]

s = "XYZdefabc"
AC = Solution().LeftRotateString(s,3)
print(AC)
