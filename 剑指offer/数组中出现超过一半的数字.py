# -*- coding: utf-8 -*-

# @Author: xyq
from collections import defaultdict
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        res = defaultdict(lambda : 0)
        size = len(numbers)
        for i in numbers:
            res[i] += 1
            if res[i] > size/2: return i
        return 0

num = [1,2,5,3,2,2,2,2]
sc = Solution().MoreThanHalfNum_Solution(num)
print(sc)



