# -*- coding: utf-8 -*-

# @Author: xyq
# 给出一个数组 nums 包含 n + 1 个整数，每个整数是从 1 到 n (包括边界)，保证至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数
# [5,5,4,3,2,1]
# 输出:
# 5
class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        i,j = 1, len(nums)-1
        while i < j:
            mid = i + (j-i)//2
            count = 0
            for elems in nums:
                if elems <= mid:
                    count += 1
            if count <= mid:
                i = mid + 1
            if count > mid:
                j = mid
        return i






