# -*- coding: utf-8 -*-

# @Author: xyq
# 返回匹配的第一个字符下标
class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # if not source and not target: return 0
        if not source and target: return -1
        if not source or not target: return 0
        table = self.getNext(target)
        i,j = 0,0
        while i < len(source) and j < len(target):
            if j == -1 or source[i] == target[j]:
                i += 1
                j += 1
            else:
                j = table[j]
        if j == len(target):
            return i - j
        else:
            return -1

    def getNext(self, target):
        j,k = 0,-1
        table = [-1] * len(target)
        while j < len(target) - 1:
            if k == -1 or target[j] == target[k]:
                k += 1
                j += 1
                # table[j] = k
                # 优化
                if target[j] != target[k]:
                    table[j] = k
                else:
                    table[j] = table[k]
            else:
                k = table[k]

        return table

s = Solution()
print(s.strStr('abcdab abcdabcdabde','abcdabd'))
