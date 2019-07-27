# -*- coding: utf-8 -*-

"""
@Time    : 2019/3/4 19:59
@Author  : Cassie
@Description :
"""


# 求最大子序列
def f(arr):
    maxsum = arr[0]
    maxhere = arr[0]
    for i in range(1, len(arr)):
        if maxhere <= 0:
            maxhere = arr[i]
        else:
            maxhere += arr[i]
        if maxhere > maxsum:
            maxsum = maxhere
    return maxsum


def g(arr):
    max = f(arr)
    for i in range(len(arr)):
        arr_new = arr[:i] + arr[i+1:]
        # print(arr_new)
        temp = f(arr_new)
        if max < temp:
            max = temp
    print(max)


if __name__ == '__main__':
    case = int(input().strip())
    for _ in range(case):
        size = int(input().strip())
        arr = list(map(int, input().strip().split()))
        g(arr)