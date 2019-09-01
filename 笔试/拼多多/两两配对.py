# -*- coding: utf-8 -*-

# @Author: xyq

n = int(input().strip())
arr = list(map(int, input().split()))
arr.sort()
plus = []
for i in range(n//2):
    plus.append(arr[i]+arr[n-1-i])

print(max(plus)-min(plus))

