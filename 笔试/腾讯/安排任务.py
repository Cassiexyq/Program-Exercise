# -*- coding: utf-8 -*-

# @Author: xyq

n,m = [int(i) for i in input().strip().split()]
machine,task = [],[]
for i in range(n):
    hours, level = [int(i) for i in input().strip().split()]
    machine.append([hours, level])
for i in range(m):
    hours,level = [int(i) for i in input().strip().split()]
    task.append([hours,level])
machine.sort(key=lambda x:(x[0],x[1]),reverse=True)
task.sort(key=lambda x:(x[0],x[1]),reverse=True)

dp = [0 for i in range(101)]
j,cnt, res = 0,0,0
# 遍历每个任务，把满足时间的任务对应的难度级别+1
# 遍历大于任务难度级别的，找到符合难度级别的
for h, l in task:
    while j < len(machine) and machine[j][0] >= h:
        dp[machine[j][1]] += 1
        j += 1
    for i in range(l,101):
        if dp[i] > 0 :
            dp[i] -= 1
            res += 200 * h + 3 * l
            cnt += 1
            break
print("%d %d" % (cnt, res))

