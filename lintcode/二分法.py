# -*- coding: utf-8 -*-

# @Author: xyq

# 找到target值
def binary_search0(arr,target):
    i,j = 0,len(arr)-1
    while i <= j:  # 加上等号，对边界值可以检测
        mid = i + (j-i)//2
        if arr[mid] < target:
            i = mid + 1
        elif arr[mid] > target:
            j = mid - 1
        else:
            return mid
    return -1


def binary_search00(arr, target):
    i,j = 0,len(arr)
    while i < j:
        mid = i + (j-i) //2
        if arr[mid] < target:
            i = mid + 1
        elif arr[mid] > target:
            j = mid
        else:
            return mid
    return -1


# 求最小的i，等于target的下标 ===  第一个大于等于target的值  == 左侧边界的二分查找
def binary_search1(arr,target):
    i,j = 0,len(arr)-1
    while i < j:
        mid = i + (j-i) // 2
        if arr[mid] < target:
            i = mid + 1
        else: j = mid
    # return i if arr[i] == target else -1
    return i


# 求最小的i ，a[i] >target
def binary_search111(arr, target):
    i,j = 0,len(arr)-1
    while i < j:
        mid = i + (j-i) //2
        if arr[mid] <= target:
            i = mid + 1
        else:
            j = mid
    return i


# 求最大的i，等于target的下标 == 最后一个小于等于target的下标 == 右侧边界的二分查找
def binary_search2(arr, target):
    i,j = 0,len(arr)-1
    while i < j:
        mid = i + (j-i+1) // 2
        if arr[mid] <= target:  
            i = mid
        else:
            j = mid-1
    return i


# 求最大的i， a[i] < target
def binary_search222(arr,target):
    i,j = 0,len(arr)-1
    while i < j:
        mid = i + (j+1-i)//2
        if arr[mid] < target:
            i = mid
        else:
            j = mid-1
    return i


if __name__ == "__main__":

    print(binary_search1([1,3,5,7,9],10))
    print(binary_search1([1,3,5,7,9],1))
    print(binary_search1([1,2,2,3,3,3,4],2))


