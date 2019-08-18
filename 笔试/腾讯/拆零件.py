# -*- coding: utf-8 -*-

# @Author: xyq
import sys
def solution(maze, e_i,e_j, i,j):
    if i == e_i and j == e_j:
        if maze[i][j] == 'X':
            return "YES"
        else:
            return "NO"
    elif i < 0 or j < 0 or maze[i][j] == 'O':
        return "NO"

    else:
        if maze[i][j] == 'X':
            maze[i][j] = 'O'
        elif maze[i][j] == '.':
            maze[i][j] = 'X'
        return solution(maze, e_i,e_j, i-1,j) or solution(maze, e_i,e_j, i, j+1) \
               or solution(maze, e_i,e_j, i+1, j) or solution(maze, e_i,e_j, i, j-1)

if __name__ == '__main__':
    case = int(sys.stdin.readline().strip())
    res = []
    for _ in range(case):
        line = sys.stdin.readline().strip()
        n,m = list(map(int,line.split()))
        maze = []
        for _ in range(n):
            maze.append(list(input().strip()))
        for i in range(n):
            maze[i][-1] = 'O'
        for i in range(m):
            maze[-1][i] = 'O'
        s_i, s_j = list(map(int, input().strip().split()))
        e_i, e_j = list(map(int, input().strip().split()))
        res.append(solution(maze, e_i-1, e_j-1,s_i-1, s_j-1))
    for i in res:
        print(i)
