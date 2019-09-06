# -*- coding: utf-8 -*-

# @Author: xyq

def solver(n,m):
    cnt_del = 0
    cnt = 0
    i = 0
    arr = [1]*n
    while cnt_del < n:
        if i == n: i=0
        if arr[i] == 1: cnt += 1
        if cnt == m:
           arr[i] = 0
           cnt = 0
           cnt_del += 1
        i += 1
    return i

print(solver(7,3))
