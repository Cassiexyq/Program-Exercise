# -*- coding: utf-8 -*-

# @Author: xyq

import math
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def isLeftCloser(self,A,target,l,r):
        if l < 0:
            return False
        if r > len(A)-1:
            return True
        if abs(A[l]-target) <= abs(A[r]-target):
            return True
        return False

    def binarySearch(self,A, target):  # 只去找左边那个不管是否最近
        i, j = 0, len(A) - 1
        while i + 1 < j:
            mid = i + math.floor((j - i) / 2)
            if A[mid] == target:
                # return A[mid]
                return mid
            if A[mid] < target:
                i = mid
            else:
                j = mid
        return i

    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A : return None
        left = self.binarySearch(A,target)
        right = left+1
        res = []
        while len(res) < k:
            if self.isLeftCloser(A, target, left, right):
                res.append(A[left])
                left -= 1
            else:
                res.append(A[right])
                right += 1
        return res

s = Solution()
res = s.kClosestNumbers([1,4,6,10,20],1,4)
print(res)





