# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak2(self, A):
        # write your code here
        if A == None or len(A) == 0:
            return -1
        for i in range(1, len(A)-1):
            if A[i] > A[i-1] and A[i+1] < A[i]:
                return i
        if A[0] > A[1]:
            return 0
        if A[-1] > A[-2]:
            return len(A)-1
        return -1

    def findPeak(self,A):
        i ,j = 0, len(A)-1
        while i < j:
            mid = (i+j)//2
            if A[mid] > A[mid+1]: j = mid
            else: i = mid+1
        return j

s = Solution()
print(s.findPeak([1,2,1,3,4,5,7,6]))