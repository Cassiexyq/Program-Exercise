# -*- coding: utf-8 -*-

# @Author: xyq

# 递增序列中找到两个数的和为s，有多组返回乘积最小的
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) == 0: return []
        j = len(array) -1
        i = 0
        res = []
        while i < j:
            if array[i] + array[j] < tsum:
                i += 1
            elif array[i] + array[j] > tsum:
                j -= 1
            else:
                res.append(array[i])
                res.append(array[j])
                break
        return res

Solution().FindNumbersWithSum([1,2,3,5,7,9,13],8)

