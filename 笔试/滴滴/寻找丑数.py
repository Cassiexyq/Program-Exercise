# -*- coding: utf-8 -*-

# @Author: xyq


def GetUglyNumber_Solution(index):
    if index <= 0: return 0
    if index == 1: return 1
    k = [1]
    t2 = t3 = t5 = 0
    for i in range(1, index + 1):
        k.append(min(k[t2] * 2, k[t3] * 3, k[t5] * 5))
        if k[i] == k[t2] * 2: t2 += 1
        if k[i] == k[t3] * 3: t3 += 1
        if k[i] == k[t5] * 5: t5 += 1
    # print(k)
    return k[index - 1]
n = int(input())
print(GetUglyNumber_Solution(n))