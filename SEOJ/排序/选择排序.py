# -*- coding: utf-8 -*-

"""
@Time    : 2019/3/25 15:20
@Author  : Cassie
@Description :
"""


def selectionsort(arr):  # 选择排序
    for i in range(len(arr)-1):
        minindex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        arr[minindex], arr[i] = arr[i], arr[minindex]
    print(arr)


def bubble(arr):  # 冒泡排序
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


def insertSort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:break
    print(arr)


if __name__ == '__main__':
    arr = [3,5,38,15,36,26,27,2,44,4]
    selectionsort(arr)
    bubble(arr)
    insertSort(arr)