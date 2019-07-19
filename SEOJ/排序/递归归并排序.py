# -*- coding: utf-8 -*-

# @Author: xyq
import math
class sort():
    def __init__(self):
        self.cn = 0

    def mergesort(self,arr):
        if len(arr) < 2:
            return arr
        mid = math.floor(len(arr)/2)
        left, right = arr[0:mid],arr[mid:]
        return self.merge(self.mergesort(left), self.mergesort(right))

    def merge(self,left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))

            else:
                result.append(right.pop(0))
                self.cn += len(left)   # 左边的 指针到最后所有的都满足
        while left: result.append(left.pop(0))
        while right: result.append(right.pop(0))
        return result

acc = [5,4,2,3]
# sort().mergesort(acc)
print(sort().mergesort(acc))