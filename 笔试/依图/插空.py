# -*- coding: utf-8 -*-

# @Author: xyq

k = int(input())
arr = list(map(int, input().split()))
cnt = 0 # 0的个数
i = 0
start = 0
res = 0
while i < len(arr):
    while i < len(arr) and arr[i] == 1:
        i += 1
    while i < len(arr) and arr[i] == 0:
        cnt += 1
        i += 1
    if cnt > 0:
        if start == 0 and i >= len(arr):
            res += (cnt+1) // 2
        elif start == 0 or i >= len(arr):
            res += cnt // 2
        else:
            res += (cnt-1)//2
    start = i
    cnt = 0
print(res)





