# -*- coding: utf-8 -*-

# @Author: xyq
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if s == None or len(s) == 0:
            return False
        res = re.match(r"[+|-]?\d*(\.\d+)?([e|E][\+|\-]?\d+)?$", s)
        if res!= None: return True
        return False

print(Solution().isNumeric("+100"))
print(Solution().isNumeric("5e2"))
print(Solution().isNumeric("-1E-16"))
print(Solution().isNumeric("12e"))
