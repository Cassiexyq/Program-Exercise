# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        i,j = 0,len(nums)
        while i < j:
            mid = i + (j-i)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1
