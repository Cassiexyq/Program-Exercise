# -*- coding: utf-8 -*-

# @Author: xyq


import sys

def caluate(arr):
    arr = [str(x) for x in arr]
    res1 = res2 = 0
    for i in arr:
        if len(i) >= 2:
            res1 += int(i[-2])
        if len(i) >= 1:
            res2 += int(i[-1])
    return min(res1,res2)
def check(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for line in sys.stdin:
    low,high = [int(x) for x in line.split()]
    res = []
    for i in range(low,high):
        if check(i):
            res.append(i)
    print(caluate(res))


