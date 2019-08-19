# -*- coding: utf-8 -*-

# @Author: xyq

# 二分法

class Solution:
    def __init__(self):
        self.data = None
        self.k = 0
    def GetNumberOfK(self, data, k):
        self.data = data
        self.k = k
        if len(self.data) == 0: return 0
        return self.getUpper() - self.getlowK() + 1

    def getlowK(self):
        start = 0
        end = len(self.data)-1

        while start <= end:
            mid = int((start + end) / 2)
            if self.data[mid] < self.k:
                start = mid+1
            else:
                end = mid
        return start

    def getUpper(self):
        start = 0
        end = len(self.data) - 1

        while start <= end:
            mid = int((start + end) / 2)
            if self.data[mid] <= self.k:
                start = mid
            else: end= mid -1
        return end

acc = [1,2,3,3,3,3]
ans = Solution().GetNumberOfK(acc, 3)
print(ans)