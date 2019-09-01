# -*- coding: utf-8 -*-

# @Author: xyq
# n=1，10
# n=2, 两位数第一位只能是1-9，第二位只能是非第一位的数，加上一位数的所有结果
# n=3, 第一位只能1-9，第二位只能是非第一位的数，第三位只能是非前两位的而结果
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n: return 1
        res,mul = 10,9
        for i in range(1,min(n,10)):
            mul *= 10 - i
            res += mul
        return res