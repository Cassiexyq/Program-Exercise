# -*- coding: utf-8 -*-

# @Author: xyq

import math

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    # 从头遍历，涉及所有情况，不是二分法
    def mountainSequence(self, nums):
        # write your code here
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]: # 当有数组头是山顶
                return nums[i-1]
            if i+1 < len(nums)-1 and nums[i] > nums[i-1] and nums[i+1] < nums[i]: # 当中间的数是山顶
                return nums[i]
            if i == len(nums)-1 and nums[i] > nums[i-1]: # 当数组尾有山顶
                return nums[i]

    def binarySearch(self,nums):
        if not nums: return -1
        if len(nums) == 1: return nums[0]
        i,j = 0,len(nums)-1
        while i+1 < j:
            mid = i + math.floor((j-i)/2)
            if nums[mid] > nums[mid-1]:
                i = mid
            if nums[mid] > nums[mid+1]:
                j = mid
            # 不存在相等的点
        return max(nums[i],nums[j])
s = Solution()
s.mountainSequence([1,2,3,5,4,1])
res = s.binarySearch([5,3,2,1])
print(res)



