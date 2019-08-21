# -*- coding: utf-8 -*-

# @Author: xyq
import sys

for line in sys.stdin:
    n = int(line)
    arr = set()
    for _ in range(n):
        arr.add(int(input()))

    new_arr = list(arr)
    new_arr.sort()
    for i in new_arr:
        print(i)

