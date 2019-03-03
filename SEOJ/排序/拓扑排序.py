# -*- coding: utf-8 -*-

"""
@Time    : 2019/2/28 9:29
@Author  : Cassie
@Description :
"""

def get_All(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

def top_sort(matrix, indegree):  # 错误
    queue = []
    result = []

    while sum(result) < len(indegree):
        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)
                indegree[i] = -1
        result.append(len(queue))
        while len(queue) > 0:
            cur = queue.pop(0)
            for j in range(len(matrix)):
                if matrix[j][0] == cur:
                    indegree[matrix[j][1]] -= 1
    jie = 1
    for ge in result:
        jie = jie*get_All(ge)
    return jie


'''
 下面是正确的
'''


def check_degree(j):
    for i in range(n): # 检查入度是否为0
        if matrix[i][j] == 1 and v[i] == 0:
            return False
    return True


def dfs(cnt):
    global num
    if cnt == n:
        num += 1
        return
    for i in range(n):
        # print(v)
        if v[i] == 0 and check_degree(i):
            v[i] = 1
            dfs(cnt+1)
            v[i] = 0


if __name__ == "__main__":
    xun_size = int(input())
    nodes = set()

    for _ in range(xun_size):
        num = 0
        pairs = input().split(',')
        for pair in pairs:
            x,y = pair.split()
            nodes.add(x)
            nodes.add(y)
        n = len(nodes)
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for pair in pairs:
            x,y = pair.split()
            matrix[ord(x)-ord('a')][ord(y)-ord('a')] = 1
        v = [0] * n
        dfs(0)

        print(num)




