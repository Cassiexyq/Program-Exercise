# -*- coding: utf-8 -*-

# @Author: xyq



def search(arr,arr2):

    if not arr or not arr2:
        return "NO"
    i = 1
    flag = 0
    while flag == 0 and i < len(arr)-1:
        if arr[i] > arr[i-1]:
            i += 1
        elif arr[i] < arr[i-1]:
            flag = 1
    arr2 = sorted(arr2)
    flag2 = 0
    for j in range(len(arr2)-1,-1,-1):
        if arr2[j] < arr[i+1] and arr2[j] > arr[i-1]:
            arr[i] = arr2[j]
            flag2 = 1
            break
        else:
            temp = i-1
            if arr2[j] < arr[temp+1] and arr2[j] > arr[temp-1]:
                arr[temp] = arr2[j]
                flag2 = 1
                break

    if flag2 == 1:
        return " ".join(list(map(str, arr)))
    else: return "NO"


if __name__ == "__main__":

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    s = search(arr1,arr2)
    print(s)
