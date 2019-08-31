# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    def longestCommonPrefix(self, strs):
        res = 0
        for i in zip(*strs):
            if len(set(i)) == 1:
                res += 1
            else:
                break
        return res
# 第一个和第二个找共同部分存res，res和第三个找共同部分
    def lCP(self, strs):
        if not strs or len(strs) == 0: return ""
        res = strs[0]
        for i in range(1, len(strs)):
            l,j = 0,0
            while l < len(res) and j < len(strs[i]) and res[l] == strs[i][j]:
                l += 1
                j += 1
            if l == 0: return ""
            res = strs[0][0:j]
        return res


s = Solution()
res = s.lCP(["flower","flow","flight"])
print(res)