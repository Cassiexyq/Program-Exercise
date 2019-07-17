# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    def multiply(self, A):
        # write code here
        # O（N^2）暴力求解
        #O（N），矩阵，左下角和右上角相乘
        res1 = [1]
        res2 = [1]
        for i in range(1, len(A)):
            num1 = A[i-1] * res1[i-1]
            num2 = A[len(A) - i] * res2[0]
            res1.append(num1)
            res2.insert(0,num2)
            # print(res1)
            # print(res2)
        for j in range(len(A)):
            res1[j] = res1[j] * res2[j]
        return res1
Solution().multiply([1,2,3,4,5])
