# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    def FindContinuousSequence(self, tsum):
        ans = []
        s = 1
        e = 2
        cur = 3
        while e < tsum:
            if cur > tsum:
                cur -= s
                s += 1
            elif cur < tsum:
                e += 1
                cur += e
            else:
                res = []
                for i in range(s, e+1):
                    res.append(i)
                ans.append(res)
                cur -= s
                s += 1
                e += 1
                cur += e
        return ans
ac = Solution().FindContinuousSequence(100)
print(ac)