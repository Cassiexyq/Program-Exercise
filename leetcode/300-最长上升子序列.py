# -*- coding: utf-8 -*-

# @Author: xyq
# 动态规划 双层遍历
# 使用 cell 保存每步子问题的最优解
# cell[i]代表第i个元素的最长上升子序列的长度
def lengthOfLIS1(nums):
    if not nums: return 0
    cell = [1]
    for i in range(1, len(nums)):
        cell.append(1)
        for j in range(i):
            if nums[j] < nums[i]:
                cell[i] = max(cell[i],cell[j]+1)
    return max(cell)

# 贪心算法 + 二分查找
# 对原序列进行遍历，将每位元素插到cell中，
# 如果 cell 中的元素都比它小，将它插到最后
# 否则，用它覆盖掉比它大的元素中最小的那个
# 一个更小的数a，后面街上一个随机数，比a大的可能性更大
import bisect
def lengthofLIS2(nums):
    size = len(nums)
    if size < 2: return size
    cell = [nums[0]]
    for num in nums[1:]:
        if num > cell[-1]:
            cell.append(num)
            continue
        # 找到第一个大于等于num的元素
        # cell[bisect.bisect_left(cell, num)] = num
        l,r = 0,len(cell)-1
        while l < r:
            mid = l + (r-l) // 2
            if cell[mid] < num:
                l = mid + 1
            else:
                r = mid
        cell[l] = num
    return len(cell)