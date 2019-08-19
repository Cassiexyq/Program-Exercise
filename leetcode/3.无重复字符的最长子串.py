# -*- coding: utf-8 -*-

# @Author: xyq

def lengthogLongestSubstring(s):
    if not s: return 0
    left = 0 # 记录窗口最左边是第几个下标
    max_len = 0
    cur_len = 0
    n = len(s)
    slide = set() # 维持最长的无重复的子串
    for i in range(n):
        cur_len += 1
        while s[i] in slide:
            slide.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len: max_len = cur_len
        slide.add(s[i])
    return max_len


