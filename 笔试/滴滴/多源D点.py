# -*- coding: utf-8 -*-

# @Author: xyq


# n,m,k = list(map(int, input().split()))
# for _ in range(k):
def los(arr):
    size = len(arr)
    if size == 0: return 0
    dp = [0]
    max_ = 0
    for i in range(size):
        tmp = 1
        for j in range(0,i):
            if arr[j] < arr[i]:
                tmp = max(tmp, 1+dp[j])
        dp.append(tmp)
        if max_ < tmp:
            max_ = tmp
    return max_

n = int(input())
arr = list(input().split())
res = los(arr)
print(res)