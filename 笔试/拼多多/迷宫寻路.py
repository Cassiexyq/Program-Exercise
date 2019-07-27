# -*- coding: utf-8 -*-

# @Author: xyq

from collections import deque
class Node:
    def __init__(self,x,y,key,step):
        self.x = x
        self.y = y
        self.key = key
        self.step = step

def bfs(i,j, maze,dir):

    q = deque()
    q.append(Node(i,j,'',0))
    while q:
        temp = q.popleft()
        if maze[temp.x][temp.y] == '3':
            return temp.step
        for k in range(4):
            res = temp.key
            nx = temp.x + dir[k][0]
            ny = temp.y + dir[k][1]
            if nx >= len(maze) or nx < 0 or ny >= len(maze[0]) or ny < 0 or maze[nx][ny] == '0':
                continue

            if maze[nx][ny].isalpha() and maze[nx][ny].islower():
                c = maze[nx][ny].upper()
                if res.find(c) == -1:
                    res += c

            if maze[nx][ny].isalpha() and maze[nx][ny].isupper() and res.find(maze[nx][ny]) == -1:
                continue

            # print(temp.step, nx, ny)
            temp_node = Node(nx, ny, res, temp.step + 1)
            q.append(temp_node)

    return 0

dir = [[0,1],[1,0],[0,-1],[-1,0]]
m,n = list(map(int, input().split()))
maze = []
for i in range(m):
    maze.append(input().strip())
col = len(maze[0])
row = len(maze)
flag = 0
for i in range(len(maze)):
    if flag == 1: break
    for j in range(len(maze[0])):
        if maze[i][j] == '2':
            print(bfs(i,j,maze,dir))
            flag = 1
            break
