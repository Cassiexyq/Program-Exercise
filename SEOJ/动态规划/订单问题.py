# -*- coding: utf-8 -*-

"""
@Time    : 2019/3/4 18:40
@Author  : Cassie
@Description :
"""
import itertools

def f(A,B,X,Y):
    res = []
    for s in range(1, X+1):
        if len(A) - s <= Y:
            res.extend(list(itertools.combinations(range(len(A)), s)))
    # print(res)

    maxum = 0
    for i in res:
        m = [0] * len(A)
        sum = 0
        for a in i:
            sum += A[a]
            m[a] = 1
        for b in range(len(B)):
            if m[b] == 0:
                sum += B[b]

        if maxum < sum:
            maxum = sum
    # print(maxum)
    return maxum


if __name__ == '__main__':
    case = int(input())
    for _ in range(case):
        N,X,Y = list(map(int, input().strip().split()))
        A = list(map(int, input().strip().split()))[:N]
        B = list(map(int,input().strip().split()))[:N]
        # print(A,B)
        max = f(A,B,X,Y)
        print(max)