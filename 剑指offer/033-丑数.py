# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0: return 0
        if index == 1: return 1
        k = [1]
        t2 =t3 =t5 = 0
        for i in range(1, index+1):
            k.append(min(k[t2] * 2, k[t3] * 3,k[t5] * 5))
            if k[i] == k[t2] * 2: t2+=1
            if k[i] == k[t3] * 3: t3+=1
            if k[i] == k[t5] * 5: t5+=1
        return k[-1]


print(Solution().GetUglyNumber_Solution(200))
