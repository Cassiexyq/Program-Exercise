# -*- coding: utf-8 -*-

# @Author: xyq

k,n = list(map(int, input().split()))
arr = [str(i) for i in range(n+1)]
if k < 0 or k > 9:
    print(0)
else:
    k = str(k)
    res = 0
    for i in range(n+1):
        if k in arr[i]:
            res += arr[i].count(k)
            # print(arr[i])
    print(res)


