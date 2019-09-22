# -*- coding: utf-8 -*-

# @Author: xyq

def multic(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return res
n = int(input())
res = multic(n)
arr = list(str(res))
# print(arr)
for i in range(len(arr)-1,-1,-1):
    if arr[i] == '0': continue
    else:
        print(arr[i])
        break

