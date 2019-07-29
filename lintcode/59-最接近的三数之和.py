# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort(key=lambda x: abs(x-target))
        print(numbers)
        return sum(numbers[:3])






s = Solution()
res = s.threeSumClosest([4,4,4,7],12)
print(res)
