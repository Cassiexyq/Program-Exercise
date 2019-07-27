# -*- coding: utf-8 -*-

"""
@Time    : 2019/3/4 20:25
@Author  : Cassie
@Description :
"""

def getMin(arr,l,h):
    res=100000000
    for i in range(l,h+1):
        if arr[i]<res:
            res=arr[i]
    return res

def minCost(arr,n):
    dp=[[0 for x in range(3)] for _ in range(n)]
    print(dp)
    for i in range(3):
        dp[0][i] = arr[0][i]
    for i in range(1,n):
        for j in range(3):
            dp[i][j]=min(getMin(dp[i-1],0,j-1), getMin(dp[i - 1], j + 1, 2))+ arr[i][j]
    res=100000000
    for i in range(3):
        if dp[n-1][i]<res:
            res=dp[n-1][i]
    return res

if __name__ == '__main__':
    case = int(input().strip())
    for _ in range(case):
        N = int(input().strip())
        res = []
        for _ in range(N):
            res.append(list(map(int, input().strip().split())))
        print(minCost(res,N))