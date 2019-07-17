# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    def StrToInt(self, s):
        if s == None or len(s) == 0:
            return 0
        if s[0] == '+' or s[0] == '-':
            isNeg = -1 if s[0] == '-' else 1
        res = 0
        for i in range(len(s)):
            if i == 0 and (s[i] == '+' or s[i] == '-'):
                continue
            if s[i] < '0' or s[i] > '9':
                return 0
            res = res * 10 + int(s[i])
        return res * isNeg

print(Solution().StrToInt("+2147483647"))