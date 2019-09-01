# -*- coding: utf-8 -*-

# @Author: xyq
# 一个数组，每个值代表这个index可以跳的步数，是否能从第一个位置跳到最后一个位置

def solution(nums):
    if not nums: return False
    k = 0
    for i in range(len(nums)):
        if i > k: return False
        k = max(k, i + nums[i])
    return True
def solution2(nums):
    if not nums: return False
    lastpoint = len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if i + nums[i] >= lastpoint:
            lastpoint = i
    if lastpoint == 0:
        return True
    else: return False
print(solution([3,2,1,0,4]))
