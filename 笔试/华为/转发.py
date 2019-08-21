# -*- coding: utf-8 -*-

# @Author: xyq

import sys


for line in sys.stdin:
    res = set()
    res.add(line.strip())
    case = int(input())
    for _ in range(case):
        temp = input().split(',')
        flag = 0
        for i in range(len(temp)):
            if flag == 1:
                break
            if temp[i] in res:
                flag = 1
                for j in range(len(temp)):
                    res.add(temp[j])

    print(len(res),end='')

