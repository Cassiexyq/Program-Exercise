# -*- coding: utf-8 -*-

# @Author: xyq


def getShort(dis):
    sum = 0
    step = 0
    while sum < dis or (sum-dis) % 2!=0:
        step +=1
        sum += step
    return step
if __name__ == '__main__':
    dis = int(input().strip())
    print(getShort(dis))