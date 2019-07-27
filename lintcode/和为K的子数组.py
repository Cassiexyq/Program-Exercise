# -*- coding: utf-8 -*-

# @Author: xyq

# 获得一个数组中连续子串和是k的个数
def getK(arr,k):
    sumd = [0] * len(arr)
    res = 0
    for i in range(len(arr)):
        if i == 0:
            sumd[i] = arr[i]
        else:
            sumd[i] = sumd[i-1] + arr[i]
        rtemp = sumd[i] - k
        if rtemp in sumd:
           res += 1
    return res

print(getK([1,1,1],2))


