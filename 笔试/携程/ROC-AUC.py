# -*- coding: utf-8 -*-

# @Author: xyq

def binary_search(arr, num):
    if num > arr[-1]:
        return len(arr)
    i,j = 0, len(arr)-1
    while i < j:
        mid = i + (j-i)//2
        if arr[mid] < num:
            i = mid + 1
        else:
            j = mid

    return i


N = int(input())
arr1 = [] # 正
arr2 = [] # 负
for _ in range(N):
    a,b = [float(x) for x in input().split()]
    if int(a) == 1:
        arr1.append(b)
    else:
        arr2.append(b)

fm = len(arr1) * len(arr2)
fz = 0
arr1.sort()
arr2.sort()
for i in range(len(arr1)):
    fz += binary_search(arr2, arr1[i])
print(round(fz/fm,2))
