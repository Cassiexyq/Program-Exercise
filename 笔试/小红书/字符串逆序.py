# -*- coding: utf-8 -*-

# @Author: xyq
from collections import deque
arr = input().split(' ')
res = []
for i in range(len(arr)):
    if arr[i].strip() == '':
        continue
    else:
        res.insert(0,arr[i])
print(' '.join(res))

