# -*- coding: utf-8 -*-

# @Author: xyq
import itertools
class Solution:
    def __init__(self):
        self.res = []
    def perm(self,n,s,e):  # 递归全排列
        if s == e: self.res.append(''.join(n))
        else:
            i = s
            for num in range(s,e):
                n[num],n[i] = n[i],n[num]
                self.perm(n, s+1, e)
                n[num],n[i] = n[i],n[num]

    def Permutation2(self, ss):
        if not ss: return []
        else:
            # res = itertools.permutations(ss)
            self.perm(ss,0,len(ss))

        return list(sorted(set(self.res)))

# c = Solution()
# ss = ['a','b','c']
# print(c.Permutation2(ss))

# 方法2取出第i个数，其他非i的数放在后面
def helper(s):
    if len(s) == 1:
        return s[0]
    res = []
    for i in range(len(s)):
        l = helper(s[:i] + s[i+1:])
        for j in l:
            res.append(s[i] + j)

    return res

def Permutation(ss):
    # write code here
    if not ss: return []
    words = list(ss)
    res = helper(words)
    return list(sorted(set(res)))

print(Permutation('abc'))