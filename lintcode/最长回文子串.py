# -*- coding: utf-8 -*-

# @Author: xyq
# 中心扩展法
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s: return -1
        strl,strr = 0, 0
        for i in range(len(s)):
            len1 = self.expand(s,i,i)
            len2 = self.expand(s,i, i+1)
            temp = max(len1,len2)
            if temp > strr-strl:
                strl = i - int((temp-1)/2)
                strr = i + int(temp /2)
        return s[strl:strr+1]

    def expand(self,s,i,j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i -1

s = Solution()
print(s.longestPalindrome("abcdzdcab"))