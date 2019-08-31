# -*- coding: utf-8 -*-

# @Author: xyq
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return -1
        strl, strr = 0, 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i + 1)
            temp = max(len1, len2)
            if temp > strr-strl:
                strl = i - (temp-1) // 2
                strr = i + temp // 2
        return s[strl:strr+1]

# def expand(s, l,r):  错误写法
#     while l >= 0 and r < len(s):
#         if s[l] == s[r]:
#             l -= 1
#             r += 1
#         else:
#             return r-l-1

    def expand(self,s,i,j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j-i-1
s = Solution()
res = s.longestPalindrome("babad")
print(res)
