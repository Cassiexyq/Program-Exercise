# -*- coding: utf-8 -*-

# @Author: xyq

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if n & 1:
    print(arr[n//2])
else:
    print(arr[n//2-1])

