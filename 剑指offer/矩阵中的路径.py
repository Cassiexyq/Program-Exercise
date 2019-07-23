# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    def __init__(self):
        self.flag = None

        self.path = []
    def hasPath(self, matrix, rows, cols, path):
        if not path:return False
        self.path = path
        self.flag = [0] * (rows * cols)
        for i in range(rows):
            for j in range(cols):
                if self.judge(matrix, rows, cols, i, j,0):
                    return True
        return False
    def judge(self, matrix,rows, cols,i,j,k):
        idx = i*cols + j
        if i < 0 or j < 0 or i >= rows or j >= cols or matrix[idx] != self.path[k] or self.flag[idx] == 1:
            return False
        if k == len(self.path)-1:
            return True
        self.flag[idx] = 1

        if self.judge(matrix, rows, cols, i-1, j,k+1) or self.judge(matrix, rows, cols, i+1, j,k+1)\
            or self.judge(matrix, rows, cols, i, j-1, k+1) or self.judge(matrix, rows, cols, i, j+1,k+1):
            return True
        self.flag[idx] = 0
        return False
s = Solution()
print(s.hasPath(['a','b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e','e'],3,4,"bcced"))

