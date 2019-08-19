# -*- coding: utf-8 -*-

# @Author: xyq
class Solution:
    def LeftRotateString(self, s, n):
        j = len(s)
        if j == 0: return ""
        if n == 0: return s
        n %= j
        return s[n:] + s[:n]

def reverse(str, s,e):
    e -= 1
    while s < e: # [s,e)
        str[s],str[e] = str[e],str[s]
        s += 1
        e -= 1
def solution(s,n):
    s = list(s)
    reverse(s,0,n)
    reverse(s, n,len(s))
    reverse(s,0,len(s))
    return ''.join(s)

s = "XYZdefabc"
AC = Solution().LeftRotateString(s,3)
print(AC)
