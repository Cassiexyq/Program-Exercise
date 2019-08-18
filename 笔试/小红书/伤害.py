# -*- coding: utf-8 -*-

# @Author: xyq
from collections import defaultdict

def caluate(s, huihe, fali, sh):
    for key, value in s.items():
        if key == 1:
            continue
        if key <= sh:  # 一次ko
            huihe -= 1 * value
            fali -= 1 * value
            if huihe >= 0 and fali >= 0:
                continue
            else:
                return False

        leiji = sh
        h, f = 1, 1
        while key > leiji:  # 一次打不下，多打几个回合
            h += 1
            f += 1
            leiji += sh
        if huihe >= h * value and fali >= f * value:
            huihe -= h * value
            fali -= f * value
        else:
            return False

    return True

n,t,m = list(map(int, input().split()))
monster = list(map(int, input().split()))
s = defaultdict(lambda:0)
for i in range(len(monster)):
    s[monster[i]] += 1

if t < n or n-s[1] > m: print(-1)
else:
    huihe = t-s[1]
    if huihe < 0 or m < huihe:
        print(-1)
    else:
        max_sh = max(monster)
        flag = False
        for i in range(2,max_sh+1):
            if caluate(s,huihe, m,i):
                print(i)
                flag = True
                break
        if not flag:
            print(-1)









