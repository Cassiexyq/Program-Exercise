# -*- coding: utf-8 -*-

# @Author: xyq
from collections import deque

if __name__ == '__main__':
    n,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if k > n: print(1)
    else:
        s = deque()
        res = []
        idx_min = 0
        temp_sum = 0
        for i in range(k):
            s.append(arr[i])
            temp_sum += arr[i]
        res.append(temp_sum)
        for i in range(k,n):
            if len(s) == k:
                temp_sum = temp_sum + arr[i] - arr[i-k]
                res.append(temp_sum)
                s.popleft()
            s.append(arr[i])
        idx = 0
        min_get = res[0]

        for i in range(1,len(res)):
            if res[i] < min_get:
                min_get = res[i]
                idx = i
        print(idx+1)





