# -*- coding: utf-8 -*-

# @Author: xyq

from collections import deque
class Solution:
    def maxInWindows(self, num, size):
        stack = deque()
        res = []
        if size > len(num) or size == 0: return []

        for i in range(size):
            while stack and num[i] >= num[stack[-1]]:
                stack.pop()
            stack.append(i)

        for i in range(size, len(num)):
            res.append(num[stack[0]])
            while len(stack) > 0 and num[i] >= num[stack[-1]]:
                stack.pop()
            while len(stack) > 0 and stack[0] < (i-size):
                stack.popleft()
            stack.append(i)
        res.append(num[stack[0]])
        return res

s = Solution()
print(s.maxInWindows([2,3,4,2,6,2,5,1],3))