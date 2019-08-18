# -*- coding: utf-8 -*-

# @Author: xyq
# 动态规划
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        res = [array[0]]
        for i in range(1, len(array)):
            res.append(max(res[i-1] + array[i], array[i]))
        return max(res)
acc = [6,-3,-2,7,-15,1,2,2]
res = Solution().FindGreatestSumOfSubArray(acc)
print(res)

