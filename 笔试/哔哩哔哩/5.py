# -*- coding: utf-8 -*-

# @Author: xyq



arr = list(input().split())
for i in range(len(arr)):
    if len(arr[i]) & 1:
        arr[i] = str(arr[i])[::-1]
print(' '.join(arr))