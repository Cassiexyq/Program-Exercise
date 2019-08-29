# -*- coding: utf-8 -*-

# @Author: xyq

# 只要 sum比target大，而且插值为偶数就可以
# 假设a为正向移动步数，b为负向移动步数，有a-b==|target|，sum==a+b；
# 则有sum-|target| == 2b;故sum与b成正比
def reachNumber(target):
    sum,i = 0,1
    a = abs(target)
    while sum < a or (sum-a) % 2 != 0:
        sum += i
        i += 1
    return i-1
