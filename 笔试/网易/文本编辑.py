# -*- coding: utf-8 -*-

# @Author: xyq
import sys
command = []
res = [[]]
a,b = 0,0
for line in sys.stdin:
    temp = line.strip().split()
    print(temp)
    if temp[0] == 'i':
        if b == 0:
            res[a].insert(b, temp[1])
            b = len(temp[1]) -1
        else:
            res[a].insert(b, temp[1])
            b = b + len(temp[-1])
    elif temp[0] == 'o':
        res.insert(a+1,temp[1])
        a = a+1
        b = len(res[a])-1
    elif temp[0] == 'a':
        if b == 0:
            res[a].extend(temp[1])
            b = len(temp[1])-1
        else:
            res[a][0].insert(b+1, temp[1])
            b = b + len(temp[1])
    elif temp[0] == 'g':
        x,y = int(temp[1])-1,int(temp[2])-1
        if x >= len(res): a = len(res)-1
        else: a = x
        if y >= len(res[a]): b = len(res[a])-1
        else: b = y
    elif temp[0] == 'd':
        n = int(temp[1])
        if len(res[a]) - b < n:
            res[a] = res[0:b+1]
            b = len(res[a])-1
        else:
            res[a] = res[a][:b+1] + res[a][b+n:]
            b = b + n - 1
    elif temp[0] == 'dd':
        del res[a]
        if a >= len(res): a = len(res)-1
        if a < 0: a = 0
        b = 0
    print(res)
    print(a,b)
