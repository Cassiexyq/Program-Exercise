# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        def quick_sort(lst):
            if not lst:return []
            privot = lst[0]
            left = quick_sort([x for x in lst[1:] if x < privot])
            right = quick_sort([x for x in lst[1:] if x > privot])
            return left + [privot] + right
        if tinput == [] or k > len(tinput): return []
        tinput = quick_sort(tinput)
        return tinput[:k]
acc = [2,3,1,5,4]
print(Solution().GetLeastNumbers_Solution(acc, 2))
