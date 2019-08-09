# -*- coding: utf-8 -*-

# @Author: xyq

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """


    def findMin(self, nums):

        length = len(nums)
        if length == 1:
            return nums[0]
        elif length > 1:
            if nums[0] < nums[-1]:
                return nums[0]
            else:
                left, right = 0, length - 1
                while right-left > 1:
                    mid = (left + right) // 2
                    if nums[mid] >= nums[left]:
                        left = mid
                    else:
                        right = mid
            return nums[right]


if __name__ == "__main__":
    s = Solution()
    # print(s.findMin([4,5,6,7,1,2,3]))
    # print(s.findMin([2,1]))
    print(s.findMin([4,5,6,7,0,1,2]))
    print(s.findMin([4,5,6,7,1,2,3]))
    print(s.findMin([2,1]))