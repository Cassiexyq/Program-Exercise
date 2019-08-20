# -*- coding: utf-8 -*-

# @Author: xyq
import math
h,w = [int(x) for x in input().split()]
img = []
for i in range(h):
    img.append([int(x) for x in input().split()])
m = int(input())
kernel = []
for i in range(m):
    kernel.append([float(x)for x in input().split()])
row = h - m + 1
col = w - m + 1
res = [[0] * col for _ in range(row)]
res_i,res_j = -1,-1
for i in range(row):
    res_i += 1
    res_j = -1
    for j in range(col):
        he = 0.0
        res_j += 1
        for x in range(m):
            for y in range(m):
                he += img[i+x][j+y] * kernel[x][y]
        res[res_i][res_j] = math.floor(he)

for i in range(row):
    for j in range(col):
        print(res[i][j],end=' ')
    print('')

