# -*- coding: utf-8 -*-

# @Author: xyq


def pick(acc):
    acc.sort()  # 按右端点排序
    # print(acc)
    res = set()
    for i in acc:
        start = i[-1]
        end = i[0]
        cn = 0
        for j in range(start, end+1):
            if j in res:  cn+=1
            if cn == 2: break
        if cn == 0:
            res.add(end-1)
            res.add(end)
        if cn == 1:
            res.add(end)
    return len(res)


if __name__ == '__main__':
    N = int(input().strip())
    acc = []
    for i in range(0,N):
        temp = list(map(int, input().strip().split(' ')))
        acc.append(temp[::-1])
    print(pick(acc))



