# -*- coding: utf-8 -*-

# @Author: xyq


# str1>str2 true
def check(str1, str2):
    if str1 == ' ' and str2 == ' ':return True
    if str1 == ' ': return True
    if str2 == ' ': return False
    i,j = 0,0
    while i < len(str1) and j < len(str2):
        if str1[i] > str2[j]:
            return True
        elif str1[i] < str2[j]:
            return False
        else:
            i += 1
            j += 1
    if j < len(str2) and i >= len(str1):
        return True
    elif j >= len(str2) and i < len(str1):
        return False
    else:
        return True


def quicksort(L,start,end):
    i = start
    j = end
    if i > j: return
    pivot = L[i]
    while i < j:
        while i < j and check(pivot, L[j]):
            j -= 1
        L[i] = L[j]
        while i < j and check(L[i],pivot):
            i = i+1
        L[j] = L[i]
    L[j] = pivot
    quicksort(L, start, i-1)
    quicksort(L, i+1, end)
    return L

arr = input().split(',')
res = quicksort(arr, 0,len(arr)-1)
print(','.join(res))
