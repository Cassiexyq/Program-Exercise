# -*- coding: utf-8 -*-

# @Author: xyq

def getBig(acc):
    acc.sort()
    maxy = acc[len(acc)-1][1]
    res = []
    for i in range(len(acc)-1, -1,-1):
        if i == len(acc)-1:
            res.append(acc[i])
            continue
        elif acc[i][1] < maxy: continue
        elif acc[i][1] >= maxy:
            maxy = acc[i][1]
            res.insert(0,acc[i])

    for j in res:
        print(str(j[0]) + ' ' + str(j[1]))


if __name__ == '__main__':
    N = int(input().strip())
    acc = []
    for i in range(N):
        acc.append(list(map(int, input().strip().split(' '))))
    getBig(acc)

