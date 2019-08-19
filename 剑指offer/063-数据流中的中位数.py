# -*- coding: utf-8 -*-

# @Author: xyq
# 每次Push进大顶堆，把大堆去除出来push进小顶堆，说明insert的数是给了小顶堆的，
# 所以当count为奇数的时候，要pop出最小的push进大顶堆，大顶堆比最小堆多一个可以
import heapq
class Solution:
    def __init__(self):
        self.count = 0
        self.max_heap = []
        self.min_heap = []
    def Insert(self, num):
        # write code here
        self.count += 1
        heapq.heappush(self.max_heap, (-num, num))
        _,max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap,max_heap_top)
        if self.count & 1: # 奇数
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

    def GetMedian(self):
        if self.count & 1:
            return self.max_heap[0][1]
        else:
            return (self.min_heap[0] + self.max_heap[0][1]) / 2.0
# 5,2,3,4,1,6,7,0,8
# 5.00 3.50 3.00 3.50 3.00 3.50 4.00 3.50 4.00
s =Solution()
s.Insert(5)
s.Insert(2)
print(s.GetMedian())
s.Insert(3)
print(s.GetMedian())
s.Insert(4)
print(s.GetMedian())
s.Insert(1)
print(s.GetMedian())