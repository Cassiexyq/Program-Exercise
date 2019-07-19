# -*- coding: utf-8 -*-

"""
@Time    : 2019/3/1 11:28
@Author  : Cassie
@Description : 计算两点之间的距离，取最近
1
3 5,6 2,5 8,9 3,8 6,1 1,2 9
8.2 4.6
2
"""
import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def to_int(n):
    return int(n) if n == int(n) else n


if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        pairs = list(map(lambda x:  list(map(float, x.split())), input().strip().split(',')))
        point = list(map(float, input().strip().split()))
        num = int(input())
        d = {}
        # print(pairs)
        for i in range(len(pairs)):
            d[i] = distance(point, pairs[i])
        d = sorted(d.items(), key=lambda x: x[1])
        # print(d)
        result = ""
        for j in range(num):
            tmp = pairs[d[j][0]]
            result += str(to_int(tmp[0]))+" " + str(to_int(tmp[1])) + ","
        print(result[:len(result)-1])

