# -*- coding: utf-8 -*-

# @Author: xyq
from collections import Counter
n,m,k = [int(x) for x in input().split()]
bb = [[0]*m for _ in range(n)]
for x in range(k):
    for i in range(n):
        temp = list(map(int,input().split()))
        for j in range(len(temp)):
            if x == 0:
                bb[i][j] = temp[j]
            else:
                if bb[i][j] == temp[j]:
                    continue
                else:
                    bb[i][j] = -1

dic = Counter(sum(bb,[]))
if dic[-1] > k:
    print(k-1)
elif -1 not in dic.items():
    print(-1)
else:
    print(dic[-1])


