# -*- coding: utf-8 -*-

# @Author: xyq
# 二进制相加
# 不算进位，相当于是两个值的异或操作，相同为0，不同为1
# 计算进位，相当于与操作，再向左移一维
# 把上两部结果进行异或再左移一位就是最终结果，知道进位为0，跳出循环
from ctypes import *
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

    def add(self,num1,num2):
        while num2 != 0:
            temp = c_int(num1 ^ num2).value
            num2 = c_int((num1 & num2) << 1).value
            num1 = temp
        return num1

print(Solution().Add(-1,2))