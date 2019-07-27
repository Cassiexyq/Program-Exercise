# -*- coding: utf-8 -*-

# @Author: xyq
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s):
        # write your code here
        if not s: return 0
        a = defaultdict(lambda :0)
        for i in s:
            a[i] += 1
        js = 0
        res = 0
        for i in a:
            if a[i] & 1:
               js += 1
               if a[i] > 1:
                   res += a[i] -1
            else:
                res += a[i]
        if js >= 1:
            res += 1
        return res
s = Solution()
print(s.longestPalindrome("aaa"))
