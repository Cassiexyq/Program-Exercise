# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    def multiply(self, A):
        # write code here
        # O（N^2）暴力求解
        # O（N），矩阵，左下角和右上角相乘
        res = [1] * len(A)
        if len(A) == 0 : return 0
        # 计算下三角
        for i in range(1,len(A)):
            res[i] = res[i-1] * A[i-1]
        temp = 1
        # 计算上三角
        for i in range(len(A)-2, -1,-1):
            temp *= A[i+1]
            res[i] *= temp
        return res

Solution().multiply([1,2,3,4,5])
