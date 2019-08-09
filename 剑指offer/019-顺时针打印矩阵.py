# -*- coding: utf-8 -*-

# @Author: xyq


def printMatrix(matrix):

    row = len(matrix) + 1
    col = len(matrix[0])+ 1
    visited = [[False] * col for _ in range(row)]
    for j in range(len(visited[-1])):
        visited[-1][j] = True
    for i in range(len(visited)):
        visited[i][-1] = True

    row = row - 1
    col = col - 1
    res = []
    i,j =0,0
    dir = 0
    while not visited[i][j]:
        res.append(matrix[i][j])
        visited[i][j] = True
        if dir == 0:
            if j < col and not visited[i][j+1]:
                j += 1
            else:
                dir = 1
                i += 1
        elif dir == 1:
            if i < row and not visited[i+1][j]:
                i += 1
            else:
                dir = 2
                j -= 1
        elif dir == 2:
            if j > 0 and not visited[i][j-1]:
                j -= 1
            else:
                dir = 3
                i -= 1
        elif dir == 3:
            if i > 0 and not visited[i-1][j]:
                i -= 1
            else:
                dir = 0
                j += 1
    return res

print(printMatrix([[1,2,3],[2,3,4],[3,4,5]]))