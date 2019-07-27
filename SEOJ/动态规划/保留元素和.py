# -*- coding: utf-8 -*-

"""
@Time    : 2019/3/4 20:52
@Author  : Cassie
@Description :
"""
def f(arr):
    rev_arr = arr[::-1]
    print(rev_arr)
    sum = 0
    while rev_arr:
        x = rev_arr.pop(0)
        sum += x
        if x - 1 in rev_arr:
            rev_arr.remove(x - 1)
    print(sum)


if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        size = int(input().strip())
        arr = list(map(int, input().strip().split()))
        f(arr)