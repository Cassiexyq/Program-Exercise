# -*- coding: utf-8 -*-

# @Author: xyq
n = int(input())
res,pre = 0,0
for i in range(5,n+1):
    while i % 5 == 0:
        i //= 5
        pre += 1
    res += pre
print(res)

