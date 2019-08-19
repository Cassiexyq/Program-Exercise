# -*- coding: utf-8 -*-

# @Author: xyq
# 哈希存储返回第一个为数量1的位置
class Solution:
    def FirstNotRepeatingChar(self, s):
        return s.index(list(filter(lambda c:s.count(c) ==1,s))[0]) if s else  -1

print(Solution().FirstNotRepeatingChar(['q','a','q']))


