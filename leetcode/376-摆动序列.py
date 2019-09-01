# -*- coding: utf-8 -*-

# @Author: xyq

# 摆动系列：插值是正负正负,得到最长的摆动序列
# 第一种 线性动态规划，记录 上升序列和下降序列

def solution1(nums):
    up = [1] * len(nums)
    down = [1] * len(nums)
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            up[i] = down[i-1]+1
            down[i] = down[i-1]
        elif nums[i] < nums[i-1]:
            down[i] = up[i-1] + 1
            up[i] = up[i-1]
        else:
            down[i] = down[i-1]
            up[i] = up[i-1]
    return max(down[-1],up[-1])

# 简化空间
def solution2(nums):
    if not nums: return 0
    up = down = 1
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            up = down + 1
        elif nums[i] < nums[i-1]:
            down = up+1
    return max(up,down)