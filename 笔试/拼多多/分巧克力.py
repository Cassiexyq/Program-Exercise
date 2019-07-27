# -*- coding: utf-8 -*-

# @Author: xyq


n = int(input())
h = list(map(int, input().split()))
m = int(input())
w = list(map(int,input().split()))
h = sorted(h)
w = sorted(w)
print(h)
print(w)
i,j = 0,0
cn = 0
while i < len(h) and j < len(w):
    if h[i] <= w[j]:
        cn += 1
        i += 1
    j += 1
print(cn)
