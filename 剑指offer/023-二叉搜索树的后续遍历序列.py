# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == None or len(sequence) == 0:
            return False
        size = len(sequence)
        root = sequence[-1]
        i = 0
        for i in range(size):
            if sequence[i] > root:
                break
        for j in range(i,size):
            if sequence[j] < root: return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        right = True
        if i < size-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])

        return left and right

so = Solution()
seq = [3,6,5,10,8]
print(so.VerifySquenceOfBST(seq))