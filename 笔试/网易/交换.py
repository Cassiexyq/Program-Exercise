# -*- coding: utf-8 -*-

# @Author: xyq

# 交换奇数偶数，只有两个加起来是奇数的可以互换不限次数，如果偶数不能交换
def solution(arr):
    temp1 = [x for x in arr if x & 1]
    temp2 = [x for x in arr if not x&1]
    if temp1 != [] and temp2 != []:
        arr.sort()
    arr = [str(x) for x in arr]
    print(' '.join(arr))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    solution(arr)

