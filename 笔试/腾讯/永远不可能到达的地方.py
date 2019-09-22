# -*- coding: utf-8 -*-

# @Author: xyq

n,m = list(map(int, input().split()))
lu = {}
for _ in range(m):
    u,v = list(map(int, input().split()))
    if u in lu:
        if v not in lu[u]:
            lu[u].append(v)
    else:
        lu[u] = [v]
    if v in lu:
        if u not in lu[v]:
            lu[v].append(u)
    else:
        lu[v] = [u]
s,t = list(map(int, input().split()))
visited = [s]
que = [[s]]
res = []
while que:
    arr = que.pop(0)
    temp = arr[-1]
    for i in range(len(lu[temp])):
        if lu[temp][i] in visited:
            continue
        if lu[temp][i] == t:
            res.append(arr+[t])
        else:
            visited.append(lu[temp][i])
            que.append(arr+[lu[temp][i]])

k = set(sum(res,[]))
ans = []
for i in range(1,n+1):
    if i in k:
        continue
    else:
        ans.append(i)
print(' '.join(map(str,ans)))



