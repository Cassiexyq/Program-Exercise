# -*- coding: utf-8 -*-

# @Author: xyq
# 必须满足这个数小于左右两个数相加
if __name__ == '__main__':
    case = int(input())
    for _ in range(case):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        if arr[-1] < arr[-2] + arr[-3]:
            print("YES")
        else:
            print("NO")




