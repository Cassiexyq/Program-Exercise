# -*- coding: utf-8 -*-

# @Author: xyq
def dfs(arr,i,j, target):
    global res
    if i >= len(arr) or j >= len(arr) or i < 0 or j < 0 or arr[i][j] != target:
        return
    if arr[i][j] == target:
        arr[i][j] = -1
        res += 1
    dfs(arr, i, j+1, target)
    dfs(arr, i, j-1, target)
    dfs(arr, i+1, j, target)
    dfs(arr, i-1, j, target)



def solver(arr, x,y):
    while arr[x][y] == -1:
        if x < len(arr):
            x += 1
        elif y >= 0:
            x = a - 1
            y -= 1
        else:
            return "empty!"
    dfs(arr, x, y, arr[x][y])



n,k = [int(x) for x in input().split()]
arr = []
res,temp = 0,0
for _ in range(n):
    arr.insert(0, list(map(int, input().split())))
for _ in range(k):
    a,b = [int(x) for x in input().split()]
    solver(arr,a-1,b-1)
    if res - temp == 1:
        print("only one!")
    elif res - temp == 0:
        print("empty!")
    else:
        print(res-temp)
    temp = res
# 5 4
# 1 2 1 4 1
# 1 1 1 1 3
# 2 4 1 2 3
# 2 5 1 3 2
# 5 2 1 5 5
# 1 2
# 1 3
# 1 5
# 3 4
