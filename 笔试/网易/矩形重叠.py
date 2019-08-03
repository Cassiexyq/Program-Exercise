# -*- coding: utf-8 -*-

# @Author: xyq



if __name__ == '__main__':
    case = int(input())
    x1 = list(map(int, input().split()))
    y1 = list(map(int, input().split()))
    x2 = list(map(int,input().split()))
    y2 = list(map(int, input().split()))
    x_set = list(set(x1+x2))
    y_set = list(set(y1+y2))
    ans = 0
    for x in x_set:
        for y in y_set:
            cnt = 0
            for i in range(case):
                if x1[i] <= x and y1[i] <= y and x2[i] > x and y2[i] > y:
                    cnt += 1
            if cnt > ans:
                ans = cnt
    print(ans)
