# -*- coding: utf-8 -*-

# @Author: xyq


def getrepeat(arr):
    i = 2
    while i < len(arr):
        temp = arr[i:]
        k,j = i,0
        while k < len(arr):
            if arr[k] == temp[j]:
                k += 1
                j += 1
            else:
                break
        if k > len(arr):
            return arr[:i]
        else:
            i += 1

    return False

size = int(input().strip())
T = input().strip()
temp = getrepeat(list(T))
print(temp)
case = int(input().strip())
res = 0
for _ in range(case):
    arr = input().strip()

    if len(arr) < temp:
        continue
    else:
        if arr == temp:
            res += 1
        else:
            if getrepeat(arr) == temp:
                res += 1
    print(res)






