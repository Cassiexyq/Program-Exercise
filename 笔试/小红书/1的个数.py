# -*- coding: utf-8 -*-

# @Author: xyq


def count(n):
    left,right,base = 0,0,1
    res = 0
    while n >= base:
        left = n // base
        right = n % base
        if (left % 10) > 1:
            res += (left // 10+1) * base
        elif (left % 10) == 1:
            res += (left // 10)*base+(right+1)
        else:
            res += (left // 10)*base
        base *= 10
    return res
res = count(34123)
print(res)