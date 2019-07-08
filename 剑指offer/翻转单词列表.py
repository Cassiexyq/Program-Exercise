# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    def ReverseSentence(self, s):

        return " ".join(s.split()[::-1]) if s.strip()!= "" else s

print(Solution().ReverseSentence("I am a student"))