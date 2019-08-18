# -*- coding: utf-8 -*-

# @Author: xyq
# 把数组中所有数字拼接起来排成一个数，打印能拼接出所有数字中最小的一个

from functools import cmp_to_key
class Solution:
    def compare(self,num1, num2):
        if num1+num2 > num2 + num1:
            return 1
        elif num1+num2 < num2 + num1:
            return -1
        else: return 0
    def PrintMinNumber(self, numbers):
        numbers = list(map(str, numbers))
        numbers.sort(key=cmp_to_key(self.compare))
        return ''.join(numbers)


print(Solution().PrintMinNumber([3,32,321]))
