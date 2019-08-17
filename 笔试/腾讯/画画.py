# -*- coding: utf-8 -*-

# @Author: xyq

n,m = [int(x) for x in input().split()]
graph = [[x for x in input().strip()] for i in range(n)]
def colorY(i,j,graph):
    while i < n and j < m:
        if graph[i][j] == 'G':
            graph[i][j] = 'B'
        elif graph[i][j] == 'Y':
            graph[i][j] = 'X'
        else:
            break
        i += 1
        j += 1

def colorB(i,j, graph):
    while i < n and j >= 0:
        if graph[i][j] == 'G':
            graph[i][j] = 'Y'
        elif graph[i][j] == 'B':
            graph[i][j] = 'X'
        else:
            break
        i += 1
        j -= 1
res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'Y' :
            colorY(i,j,graph)
            res += 1
        elif graph[i][j] == 'B':
            colorB(i,j,graph)
            res += 1
        elif graph[i][j] == 'G':
            colorY(i,j,graph)
            colorB(i,j,graph)
            res += 2
        else:
            continue
print(res)

