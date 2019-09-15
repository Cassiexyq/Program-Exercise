# -*- coding: utf-8 -*-

# @Author: xyq
from functools import cmp_to_key
def cmp_check(s1,s2):
    m1,m2 = s1[0] * s1[1],s2[0]*s2[1]
    if m1 == m2:
        wh1 = min(s1[0]*1.0/s1[1],s1[1]*1.0/s1[0])
        wh2 = min(s2[0]*1.0/s2[1],s2[1]*1.0/s2[0])
        if wh1 == wh2:
            if s1[0] > s2[0]: return 1
            elif s1[0] < s2[0]: return -1
            else: return 0
        elif wh1 > wh2: return -1
        else: return 1
    elif m1 < m2: return -1
    else: return 1

n = int(input())
arr = list(map(int, input().split()))
jx = []
for i in range(n):
    s1 = arr.pop(0)
    s2 = arr.pop(0)
    jx.append([s1,s2])
jx.sort(key=cmp_to_key(cmp_check))
# print(jx)
print(' '.join(map(str,sum(jx,[]))))