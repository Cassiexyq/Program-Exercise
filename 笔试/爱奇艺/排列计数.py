# -*- coding: utf-8 -*-

# @Author: xyq
def dfs(n, yq):
    queue = [[i] for i in range(1,n+1)]
    for i in range(len(yq)):
        while queue and len(queue[0]) == (i+1):
            temp = queue.pop(0)
            idx = temp[-1]
            if yq[i] == 1:
                if idx == 1: continue
                else:
                    for num in range(idx-1,0,-1):
                        if num not in temp:
                            queue.append(temp + [num])
            else:
                if idx == n: continue
                else:
                    for num in range(idx+1, n+1):
                        if num not in temp:
                            queue.append(temp +[num])

    return queue

n = int(input())
yq = list(map(int, input().split()))
res = dfs(n,yq)
print(len(res) % (10 ** 9 + 7))


