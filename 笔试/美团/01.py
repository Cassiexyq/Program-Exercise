# -*- coding: utf-8 -*-

# @Author: xyq

n,k = list(map(int,input().split()))
num = list(map(int,input().split()))
i,j =0,0
res = 0
while j<n:
    if num[j]==1:
        j += 1
    elif k > 0:
        k -= 1
        j += 1
    else:
        res = max(res,j-i)
        while i<j and num[i]==1:
            i += 1
        j += 1
        i += 1
res = max(res,j-i)
print(res)

