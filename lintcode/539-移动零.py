# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    思路：
快慢指针：假设我们有一个新数组，有 2 根指针分别从老数组和新数组从前往后走，称老数组上的指针为「读指针」，
新数组上的指针为「写指针」；只有当读指针所指向的数值非0时，才将读指针所指的数值写入到写指针所指的空间上，
然后两根指针再继续向前走；当老数组遍历完时，只要将新数组继续填 0 直到新老数组长度一致即可。
题目要求「就地操作」，那么实际上就不需要开这个新数组，只要让两根指针都在原数组上往前走就行：这
是因为，读指针由于会跳过非 0 空间，其扫描速度远快于写指针，
所有被读指针扫描过的非零值都会通过写指针写入「新的空间」中，因此所有被写指针覆盖掉的非零值，
之前必定已经保存过了。该方法时间复杂度 O(n)，空间复杂度 O(1)
    """
    def moveZeroes(self, nums):
        # write your code here
        if len(nums) == 1:
            return nums
        i = j = 0
        while i < len(nums):
            if nums[i] != 0:  # 也就是说i会跳过0值不写入
                nums[j] = nums[i]
                j += 1
            i += 1
        while j < i:
            nums[j] = 0
            j += 1
        return nums
s = Solution()
res = s.moveZeroes([-1,2,-3,4,0,1,0,-2,0,0,1])
print(res)



