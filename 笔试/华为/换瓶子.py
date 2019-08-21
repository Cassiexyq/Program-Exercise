# -*- coding: utf-8 -*-

# @Author: xyq
import sys
def helper(n):
    res = 0
    while n >= 2:
        if n == 2:
            res += 1
            n = 0
        drink = n // 3
        res += drink
        n = drink + n % 3
    return res


for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    print(helper(n))

