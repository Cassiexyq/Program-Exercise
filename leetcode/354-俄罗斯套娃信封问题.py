# -*- coding: utf-8 -*-

# @Author: xyq

# 把所有信封（w,h）,按w升序，相同w按h降序处理，在h上实现最长上升子序列
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        size = len(envelopes)
        if size < 2:
            return size
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        height = [i[1] for i in envelopes]
        tail = [height[0]]
        for i in range(1,len(height)):
            if height[i] > tail[-1]:
                tail.append(height[i])
                continue
            else:
                l,r = 0,len(tail)-1
                while l < r:
                    mid = l + (r - l) // 2
                    if tail[mid] < height[i]:
                        l = mid + 1
                    else:
                        r = mid
                tail[l] = height[i]
        return len(tail)

s = Solution()

res = s.maxEnvelopes([[30, 50], [12, 2], [3, 4], [12, 15]])
print(res)


