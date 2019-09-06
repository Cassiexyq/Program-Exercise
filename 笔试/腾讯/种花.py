# -*- coding: utf-8 -*-

# @Author: xyq


case, k = list(map(int, input().split()))
for _ in range(case):
    a,b = list(map(int, input().split()))
    if a <= b:
        ji = 0
        res = 0
        while k * ji <= b:
            bai = k * ji
            if ji == 0:
                res += b - a + 1
            else:
                if bai >= a: hong_min = 0
                else:
                    hong_min = a-k*ji
                hong_max = b - k * ji
                for i in range(hong_min,hong_max+1):
                    if i == 0:
                        res += 1
                    else:
                        res += i+1

            ji += 1
        print(res)




