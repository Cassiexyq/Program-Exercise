# -*- coding: utf-8 -*-

# @Author: xyq

# 有障碍物不能走，从起点（0，0）到给定的终点最少的步数
r,c,n = list(map(int, input().split()))
matrix = {}
for _ in range(n):
    a,b = list(map(int, input().split()))
    matrix[(a,b)] = 1
visited = {}
def bfs():
    from collections import deque
    que = deque([(0,0)])
    visited[(0,0)] = 1
    cnt = 0
    while que:
        temp = deque()
        while que:
            cur = que.popleft()
            for a,b in [[0,1],[1,0],[-1,0],[0,-1]]:
                nxt = (cur[0]+a,cur[1]+b)
                if nxt[0] == r and nxt[1] == c:
                    return cnt + 1
                if nxt not in visited and nxt not in matrix:
                    visited[nxt] = 1
                    temp.append(nxt)
        que = temp
        cnt += 1
print(bfs())


