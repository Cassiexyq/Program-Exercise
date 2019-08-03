# -*- coding: utf-8 -*-

# @Author: xyq

def LastPosition(nums,target):
    i,j = 0,len(nums)-1
    while i < j:
        mid = (i+j)//2
        if nums[mid] <= target:
            i = mid+1
        else:
            j = mid-1
    if i > 0 and nums[i-1] == target and nums[i] != target:
        return i-1
    return i

def FirstPosition(nums,target):
    i,j = 0,len(nums)-1
    while i < j:
        mid = (i+j) // 2
        if nums[mid] < target:
            i = mid +1
        else:
            j = mid -1
    if j < len(nums)-1 and nums[j+1] == target and nums[j] != target:
        return j+1
    # else:
    return j



res1 = LastPosition([1,2,2,2,5,5],2)
print(res1)
res2 = FirstPosition([1,2,2,2,5,5],2)
print(res2)