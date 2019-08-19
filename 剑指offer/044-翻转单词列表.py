# -*- coding: utf-8 -*-

# @Author: xyq
# 考虑用栈存储，然后弹出
class Solution:
    def ReverseSentence(self, s):

        return " ".join(s.split()[::-1]) if s.strip()!= "" else s

print(Solution().ReverseSentence("I am a student"))