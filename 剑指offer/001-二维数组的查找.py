# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        col = len(array[0])
        row = len(array)

        i,j = row-1,0
        while i >= 0 and j < col:
            if array[i][j] < target:
                j += 1
            elif array[i][j] > target:
                i -= 1
            else:
                return True
        return False

