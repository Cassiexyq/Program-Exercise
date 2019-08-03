# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    # 时间复杂度O(n)  空间复杂度O(n)
    def deduplication(self, nums):
        # write your code here

        num_set = set()
        i = 0
        for num in nums:
            if num not in num_set:
                num_set.add(num)
                nums[i] = num
                i += 1
        return nums


    # 双指针， 时间复杂度O(nlogn)
    def ded(self,nums):
        self.quicksort(nums, 0, len(nums)-1)
        i = j = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return nums

    def quicksort(self,nums, start, end):
        if start < end:
            pivot = start
            left,right = start+1, end
            while left <= right:
                while left <= right  and nums[pivot] >= nums[left]:
                    left += 1
                while left <= right and nums[pivot] <= nums[right]:
                    right -= 1
                if left <= right:
                    nums[left],nums[right] = nums[right],nums[left]
            nums[pivot],nums[right] = nums[right],nums[pivot]
            self.quicksort(nums,start, right-1)
            self.quicksort(nums,right+1,end)
        else:
            return
s = Solution()
print(s.deduplication([1,3,1,4,4,2]))
print(s.ded([1,3,1,4,4,2]))
