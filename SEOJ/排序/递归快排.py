# -*- coding: utf-8 -*-

# @Author: xyq


def bubble(array):
    flag = 0

    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = 1
        if flag == 0:
            break
    return array

def selectsort(array):
    for i in range(len(array)-1):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

def insetsort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array

def heap(L):
    L.insert(0,0)
    size = len(L)
    idx = int((size-1)/2)
    for i in range(idx,0,-1):
        adjust_down(L, i, size-1)
    for j in range(1, size-1):
        L[1], L[size-j] = L[size-j], L[1]
        adjust_down(L, 1, size-j-1)
    return L[1:]

def adjust_down(L,start, end):
    temp = L[start]
    i = start
    j = 2 * i

    while j <= end:
        if j < end and L[j] < L[j+1]:
            j = j + 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else: break
    L[i] = temp


def quicksort(L,s,e):
    i = s
    j = e
    if i > j: return
    pivot = L[i]
    while i < j:
        while i < j and pivot <= L[j]:
            j -= 1
        L[i] = L[j]
        while i < j and pivot >= L[i]:
            i = i+1
        L[j] = L[i]
    L[i] = pivot
    quicksort(L, s,i-1)
    quicksort(L, i+1, e)
    return L

def quick(L):
    stack = []
    stack.append(len(L)-1)
    stack.append(0)
    while stack:
        left = stack.pop()
        right = stack.pop()
        idx = partition(L, left, right)
        if idx > left:
            stack.append(idx-1)
            stack.append(left)
        if idx < right:
            stack.append(right)
            stack.append(idx+1)
    return L

def partition(L, start, end):
    pivot = L[start]
    while start < end:
        while start < end and pivot <= L[end]:
            end -= 1
        L[start] = L[end]
        while start < end and pivot >= L[start]:
            start += 1
        L[end] = L[start]
    L[start] = pivot
    return start
import math

def merge(L):
    if len(L) < 2: return L
    mid = math.floor(len(L) / 2)
    left, right = L[0:mid], L[mid:]
    return merge_sort(merge(left), merge(right))

def merge_sort(left, right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left: res.append(left.pop(0))
    while right: res.append(right.pop(0))
    return res

def merge2(L):
    i = 1 # step
    while i < len(L):
        low = 0
        while low < len(L):
            mid = low + i
            height = min(low + 2 * i, len(L))
            if mid < height:
                merge_sort2(L, mid,low, height)
            low += 2 * i
        i *= 2
    return L

def merge_sort2(L, mid, left, right):
    res = []
    i = L[left: mid]
    j = L[mid: right]
    while i and j:
        if i[0] <= j[0]:
            res.append(i.pop(0))
        else:
            res.append(j.pop(0))
    if i: res += i
    if j: res += j
    L[left: right] = res


arr = [3,5,38,15,36,26,27,2,44,4]
# print(arr)
# print(bubble(arr))
# print(selectsort(arr))
# print(insetsort(arr))
print(quicksort(arr, 0, len(arr)-1))
print(quick(arr))
print(merge(arr))
print(merge2(arr))
print(heap(arr))

