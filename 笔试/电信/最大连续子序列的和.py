# -*- coding: utf-8 -*-

# @Author: xyq

line = input().replace("[","").replace("]","")
arr = list(map(int,line.split(',')))
if len(arr) == 0: print(0)
else:
    dp = [0]*len(arr)
    dp[0] = arr[0]
    for i in range(1,len(arr)):
        dp[i] = max(dp[i-1]+arr[i],arr[i])
    print(max(dp))

