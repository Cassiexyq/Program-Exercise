# -*- coding: utf-8 -*-

# @Author: xyq
# 非递减排序的数组，对某个值进行旋转
# 注意非递减数组包括重复情况，分三种情况，mid>=左边，往右边找，Mid<左边，往左边找
# ，当 j-i==1，说明找到了最大最小的位置，返回j, 当三个指针都相等，只能遍历
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0: return 0
        if len(rotateArray) == 1: return rotateArray[0]
        i,j = 0,len(rotateArray)-1
        while j-i >1:
            mid = i + (j-i)//2
            if rotateArray[mid] == rotateArray[i] == rotateArray[j]:
                return min(rotateArray[i:j+1])

            if rotateArray[mid] >= rotateArray[i]:
                i = mid
            elif rotateArray[mid] < rotateArray[i]:
                j = mid
        return rotateArray[j]

        # res = min(rotateArray[i], rotateArray[j])
        # return res
    def MinInorder(self, arr, left, right):
        res = 0
        print(left, right)
        for i in range(left, right +1):
            if res > arr[i]:
                res = arr[i]
        return res
s = Solution()
print(s.minNumberInRotateArray([2,2,2,1,1]))
print(s.minNumberInRotateArray([3,3,3,1,2]))
print(s.minNumberInRotateArray([2,2,0,1,1,1]))
print(s.minNumberInRotateArray([3,4,5,1,2]))