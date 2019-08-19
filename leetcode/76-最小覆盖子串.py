# -*- coding: utf-8 -*-

# @Author: xyq

# 从S中找出一个包含T所有字母的最小子串
from collections import defaultdict
def minWindow(s,t):
    start,minLen = 0, float('inf')
    left,right = 0,0
    window =defaultdict(int)
    needs = defaultdict(int)
    for i in t:
        needs[i] += 1
    match = 0
    while right < len(s): # 只有当窗口内包含了所有要求的字母后进行第二部缩小窗口
        temp = s[right]
        if temp in needs.keys():
            window[temp] += 1
            if window[temp] == needs[temp]:
                match += 1
        right += 1

        while match == len(needs): # 记录每次移动的长度，满足条件是当前窗口满足包含了所有字母
            if right - left < minLen:  # 更新最小长度，记录长度和第一个下标
                start = left
                minLen = right -left
            temp = s[left]
            if temp in needs.keys():  # 查看是否还满足包含所有字母
                window[temp] -= 1
                if window[temp] < needs[temp]:
                    match -= 1
            left += 1
    return ''.join(s[start: start+minLen]) if minLen != float('inf') else ''
