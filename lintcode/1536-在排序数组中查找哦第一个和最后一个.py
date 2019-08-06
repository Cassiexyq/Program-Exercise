# -*- coding: utf-8 -*-

# @Author: xyq



class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        i,j = 0, len(nums)
        while i < j:
            mid = i + (j-i) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        if nums[i] == target:
            res = [i]
            end = i+1
            while end < len(nums):
                if nums[end] == target:
                    end += 1
                else:
                    end -= 1
                    break
            res.append(end)
            return res
        else:
            return [-1,-1]