# -*- coding: utf-8 -*-

# @Author: xyq
# 给定一个整数数组，找到一个具有最大和的连续子数组
def solution(nums):
    if len(nums) == 1: return nums[0]
    res = [nums[0]]
    for i in range(1,len(nums)):
        res.append(max(res[i-1]+nums[i], nums[i]))
    return max(res)
print(solution([-2,1,-3,4,-1,2,1,-5,4]))