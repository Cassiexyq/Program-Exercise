# -*- coding: utf-8 -*-

# @Author: xyq

import sys
def getMoney(job, case):
    i = 0
    while i < len(job):
        if case > job[i][0]:
            i += 1
            continue
        elif case == job[i][0]:
            return job[i][1]
        else:
            return job[i-1][1]


if __name__ == '__main__':
    N,M = [int(x) for x in input().split()]
    job = []
    while len(job) != N:
        line = input()
        if line == '':
            continue
        job.append([int(x) for x in line.split()])
    line = input()
    if line == '':
        line = input()
    job.sort()
    people = list(map(int, line.split()))
    # 把能力小的报酬多的话，就把报酬多的给能力大的   更新报酬
    for i in range(1, len(job)):
        if job[i-1][1] > job[i][1]:
            job[i][1] = job[i-1][1]
    ability = [i[0] for i in job]
    ans = []
    import bisect
    for i in people:
        # 找到能力大一点的那个位置
        idx = bisect.bisect_right(ability,i)-1
        if idx == -1:
            ans.append(0)
        else:
            ans.append(job[idx][1])
    for i in range(len(ans)):
        print(ans[i])



