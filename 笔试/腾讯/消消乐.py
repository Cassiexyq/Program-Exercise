# -*- coding: utf-8 -*-

# @Author: xyq

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    res = []
    for _ in range(n):
        size = int(sys.stdin.readline().strip())
        arr = list(map(int, sys.stdin.readline().strip().split()))
        arr.sort()
        i,j = 0,len(arr)-1
        flag = 1
        while i < j:
            if arr[i] != arr[j]:
                i += 1
                j -= 1
            else:
                flag = 0
                break
        if flag:
            res.append("YES")
        else: res.append("NO")
    for i in range(n):
        print(res[i])






