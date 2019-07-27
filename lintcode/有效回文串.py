# -*- coding: utf-8 -*-

# @Author: xyq
# 415

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if not s: return True
        s = "".join(filter(str.isalnum, s))
        s = s.lower()
        i,j = 0, len(s)-1
        while i < j:
            if i < j and s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        if i >= j: return True
        else: return False

s = Solution()
print(s.isPalindrome("ab"))
