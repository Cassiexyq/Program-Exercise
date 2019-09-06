# -*- coding: utf-8 -*-

# @Author: xyq

n = int(input().strip())
m = int(input().strip())
time = [[0]*n for _ in range(n)]
res = []
for i in range(m):
    a,b,t = [int(x) for x in input().strip().split()]
    res.append([a,b,t])
    res.append([b,a,t])
    time[a][b] = t
    time[b][a] = t
res.sort(key=lambda x: (x[0],x[2]))
dic = dict()
for i in range(len(res)):
    if res[i][0] not in dic:
        dic[res[i][0]] = [res[i][1]]
    else:
        dic[res[i][0]].append(res[i][1])
queue = [0]
start = 0
flag = 0
ans = 0
while len(queue) != n:
    if start not in dic:
        flag = 0
        break
    for i in dic[start]:
        flag = 0
        if i not in queue:
            queue.append(i)
            ans += time[start][i]
            start = i
            flag = 1
            break
    if flag == 0:
        break
if flag == 0:
    print(-1)
else:
    ans += time[queue[-1]][0]
    print(ans)







