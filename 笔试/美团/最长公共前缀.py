# -*- coding: utf-8 -*-

# @Author: xyq

def check(a,b):
    i,j = 0,0
    mx = 0
    temp = 0
    while a[i] == b[j] and i < len(a) and j < len(b):
        i += 1
        j += 1
        temp += 1
    mx = max(temp, mx)

    return mx

# 两个都为空 就是 1
import sys
n = int(input())
res = []
for _ in range(n):
    res.append(input().split())
for line in sys.stdin:
    s1,s2 = list(map(int,line.strip().split(' ')))
    a,b = res[s1-1][0], res[s2-1][0]
    if 0 <= len(a) < n-1 and 0 <= len(b) < n-1:
        print(check(a,b))



