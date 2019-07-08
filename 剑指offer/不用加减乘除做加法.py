# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    def Add(self, num1, num2):
        # if num2 == 0:
        #     return num1
        # else:
        #     return self.Add(num1^num2, (num1&num2) << 1)
        while num2 != 0:
            temp = (num1 ^ num2) & 0xffffffff
            num2 = ((num1 & num2) << 1) & 0xffffffff
            num1 = temp
        return num1 if num1 <= 0x7fffffff else ~(num1^0xffffffff)

print(Solution().Add(-1,2))