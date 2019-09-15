# -*- coding: utf-8 -*-

# @Author: xyq

a,b = list(map(int, input().split()))
res = []
for _ in range(b):
    temp = list(map(int, input().split()))
    res.append(temp)
for i in range(b):
    if i == 0:
        idx = res[i].index(min(res[i]))
        if idx == 1:
            temp = res[i].pop(0)
            res[i].append(temp)
        else:
            temp = res[i].pop(-1)
            res[i].insert(0,temp)
    else:
        res[i].sort()
    print(' '.join(map(str, res[i])))

