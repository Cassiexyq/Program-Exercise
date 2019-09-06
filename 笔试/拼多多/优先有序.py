# -*- coding: utf-8 -*-

# @Author: xyq

def quicksort(L,s,e): # 从大到小排序
    i = s
    j = e
    if i > j: return
    pivot = L[i]
    while i < j:
        while i < j and check(pivot,L[j]):
            j -= 1
        L[i] = L[j]
        while i < j and check(L[i],pivot):
            i = i+1
        L[j] = L[i]
    L[j] = pivot
    quicksort(L, s, i-1)
    quicksort(L, i+1, e)
    return L
def checkJO(num):
    if num & 1: return True
    else: return False
def check(num1,num2):
    s1 = checkJO(num1)
    s2 = checkJO(num2)
    if (s1 and s2) or (not s1 and not s2): # 都是奇数或偶数
        return True if num1 > num2 else False
    else:
        return True if not s1 else False


while True:
    try:
        line = input().strip()
        arr, n = line.split(';')
        arr = list(map(int,arr.split(',')))
        n = int(n)
        L = quicksort(arr, 0,len(arr)-1)
        print(','.join(map(str,L[:n])))
    except:
        break


