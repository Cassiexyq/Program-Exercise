# -*- coding: utf-8 -*-

# @Author: xyq
import itertools
class Solution:

    def Permutation2(self, ss):
        result = []
        if not ss: return []
        else:
            res = itertools.permutations(ss)
            for i in res:
                if ''.join(i) not in result:
                    result.append(''.join(i))
        return result



c = Solution()
ss = ['a','b','a']
print(c.Permutation(ss))

