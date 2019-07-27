# -*- coding: utf-8 -*-

# @Author: xyq

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素


def getmin(arr):

    if len(arr) == 1 or arr[-1] > arr[0]:
        return arr[0]

    h = len(arr)-1
    l = 0
    while l < h:

        mid = l + int((h-l)/2)
        if arr[mid] > arr[mid+1]:
            return arr[mid+1]
        if arr[mid-1] > arr[mid]:
            return arr[mid]
        if arr[l] < arr[mid]:
            l = mid + 1
        elif arr[l] > arr[mid]:
            h = mid - 1

