# -*- coding: utf-8 -*-

# @Author: xyq

# 所有房屋围城一个圈，相邻的不能偷，也就是出来里面相邻不能之外，首尾也是相邻的
# 就掐头dp一次，去尾dp一次

def rob(nums):
    def roober(arr):
        size = len(arr)
        if size == 0: return 0
        if size == 1: return arr[0]
        dp = [0] * size
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
        return max(dp)
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0],nums[1])
    max1 = roober(nums[:-1])
    max2 = roober(nums[1:])
    return max(max1,max2)

def solution(nums):
    def robber(arr):
        pre, cur = 0, 0
        for i in arr:
            pre, cur = cur, max(pre + i, cur)
        return cur

    if len(nums) == 1: return nums[0]
    return max(robber(nums[1:]), robber(nums[:-1]))

res = rob([2,3,2])
print(res)

