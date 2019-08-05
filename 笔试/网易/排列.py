# -*- coding: utf-8 -*-

# @Author: xyq
# 按字典序全排列，告诉你一个排序顺序为第Q个，输出倒数第Q个排列
if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().strip().split()]
    values = list(map(int, input().split()))
    res = []
    for v in values:
        res.append(n+1-v)
    res = [str(x) for x in res]
    print(' '.join(res))



