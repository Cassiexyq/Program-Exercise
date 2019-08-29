# -*- coding: utf-8 -*-

# @Author: xyq
import math
def helper(target):
    sum,n = 0,0
    # target = abs(target)
    if target < 0:
        return 0
    while (1):
        if sum >= target:
            if sum == target or (sum-target) % 2 == 0:
                return n
            elif n % 2 == 0:
                return n+1
            else:
                return n +2
        n += 1
        sum += n

    # if n < 0:
    #     n = -n
    # i = 0
    # while i*(i+1) //2 < n:
    #     i += 1
    # if i*(i+1) // 2 == n:
    #     return i
    # else:
    #     if (i*(i+1)//2-n) % 2 == 0:
    #         return i
    #     else:
    #         if i % 2 == 0: return i+1
    #         else: return i+2
n = int(input())
print(helper(n))

