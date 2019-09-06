# -*- coding: utf-8 -*-

# @Author: xyq

def LastPosition(nums,target): # 右侧边界的查找
    i,j = 0,len(nums)-1
    while i < j:
        mid = i + (j-i+1) // 2
        if nums[mid] <= target:
            i = mid
        else:
            j = mid-1
    return i

def FirstPosition(nums,target): # 左侧边界的查找
    i,j = 0,len(nums)-1
    while i < j:
        mid = (i+j) // 2
        if nums[mid] < target:
            i = mid +1
        else:
            j = mid
    return i



res1 = LastPosition([1,2,2,2,5,5],6)
print(res1)
res2 = FirstPosition([1,2,2,2,5,5],6)
print(res2)