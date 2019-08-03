# -*- coding: utf-8 -*-

# @Author: xyq

def check2(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            return True
    return False
def check3(arr1, arr2):
    flag = 0
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            flag += 1
        if flag == 2:
            return True
    return False

def check(arr):
    if len(arr) == 2:
        return check3(arr[0],arr[1])
    else:
        for i in range(len(arr)-1):
            if i == len(arr)-1:
                flag = check2(arr[i],  arr[0])
            else:
                flag = check2(arr[i], arr[i+1])

            if not flag:
                    return False
    return True
def check4(arr):
    if len(arr) == 2:
        if arr[0][0] == arr[1][-1] and arr[0][-1] == arr[1][0]:
            return True
        else: return False
    for i in range(1,len(arr)-1):
        if i == len(arr)-1:
            if arr[i][-1] == arr[0][0]:
                continue
            else:
                return False
        else:
            if arr[i][0] == arr[i-1][-1]:
                continue
            else:
                return False
    return True


if __name__ == '__main__':

    line = input().strip()
    arr = line.split()
    ans = check4(arr)
    print(ans)
