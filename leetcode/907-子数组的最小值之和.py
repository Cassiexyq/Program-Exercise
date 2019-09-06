# -*- coding: utf-8 -*-

# @Author: xyq


# 对于一个数组，所有可能的子集，每个子集的最小值相加，这个子集是要连续子序列

def solver(A):
    left = [0]*len(A)
    right = [0]*len(A)
    stack = []
    for i in range(len(A)):
        while stack and A[stack[-1]] > A[i]:
            stack.pop()
        if not stack:
            left[i] = -1
        else:
            left[i] = stack[-1]
        stack.append(i)
    stack = []
    for i in range(len(A)-1,-1,-1):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()
        if not stack:
            right[i] = len(A)
        else:
            right[i] = stack[-1]
        stack.append(i)
    ans = 0  # A[left+1:right]
    for i in range(len(A)):
        ans += (i-left[i]) * (right[i] - i) * A[i]
    return ans % (10**9+7)



print(solver([3,1,2,4]))