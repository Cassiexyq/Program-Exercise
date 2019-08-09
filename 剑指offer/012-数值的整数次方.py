# -*- coding: utf-8 -*-

# @Author: xyq

def power(base, exponent):
    p = abs(exponent)
    res = 1.0
    while p:
        if p & 1: res *= base
        base *= base
        p = p >> 1
    return res if exponent > 0 else 1/res

