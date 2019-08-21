# -*- coding: utf-8 -*-

# @Author: xyq

import sys

# for line in sys.stdin:
arr = input().split()
if arr[0] == 0:
    print(0)
else:
    res = ['0']
    for i in range(1,len(arr)):
        arr[i] = int(arr[i],16)
        if arr[i] == 10:
            res.append(18)
            res.append(19)
        elif arr[i] == 11:
            res.append(171)
            res.append(205)
        else:
            res.append(arr[i])
    for i in range(1,len(res)):
        res[i] = hex(res[i])[2:]
    if len(res) > 10:
        res[0] = hex(len(res))[2:]
    print(' '.join(res).upper(),end='')



