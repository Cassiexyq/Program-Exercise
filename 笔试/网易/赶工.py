# -*- coding: utf-8 -*-

# @Author: xyq
def solve(res):
    ans, total = 0, 0
    for i in range(n):
        if total + res[i][1] > res[i][0]:
            ans += (total + res[i][1] - res[i][0])
        total += res[i][1]
    return ans
n = int(input())
res = []
for _ in range(n):
    res.append(list(map(int, input().split())))
res1 = sorted(res,key=lambda x:(x[0],-x[1]))
res2 = sorted(res,key=lambda x:(x[0],x[1]))
print(min(solve(res1),solve(res2)))


