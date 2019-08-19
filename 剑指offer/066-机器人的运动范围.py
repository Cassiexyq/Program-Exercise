# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    def __init__(self):
        self.flag = []
    def movingCount(self, threshold, rows, cols):
        for i in range(rows):
            temp = [0] * cols
            self.flag.append(temp)
        return self.helper(0, 0, rows, cols, threshold)
    def helper(self, i, j, rows, cols, threshold):
        if i < 0 or i >= rows or j < 0 or j >= cols or not self.check(threshold, i,j) or self.flag[i][j] == 1:
            return 0
        self.flag[i][j] = 1
        return self.helper(i+1,j, rows, cols, threshold) + self.helper(i-1, j, rows, cols, threshold) \
               + self.helper(i, j-1, rows, cols, threshold) + self.helper(i, j+1, rows, cols, threshold) + 1

    def check(self,threshold, i,j):
        res = self.getNum(i) + self.getNum(j)
        # print("{},{} = {}".format(i,j, res))
        if res <= threshold: return True
        else: return False
    def getNum(self, i):
        res = 0
        x = i / 10
        if x == 0:
            res += i
        else:
            while i > 0 :
                res += (i % 10)
                i = int(i / 10)
        return res

s = Solution()
print(s.movingCount(5,10,10))