# -*- coding: utf-8 -*-

# @Author: xyq

n = int(input())
res = 0
while n:
    if n & 1:
        res += 1
    n = n >> 1
print(res % 1000003)
