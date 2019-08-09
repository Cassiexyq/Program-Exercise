# -*- coding: utf-8 -*-

# @Author: xyq
# 遇到奇数往前比较，遇到偶数就交换
def reorder(arr):
    size = len(arr)
    for i in range(size):
        if arr[i] & 1:
            k = i
            while k > 0 and not arr[k-1] & 1:
                arr[k], arr[k-1] = arr[k-1],arr[k]
                k -= 1
    return arr
print(reorder([2,4,1,10,3,5,6,8]))

