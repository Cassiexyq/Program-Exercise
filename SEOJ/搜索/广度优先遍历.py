# -*- coding: utf-8 -*-

"""
@Time    : 2019/2/26 13:41
@Author  : Cassie
@Description :
"""


def bfs(matrix,s,n, node):
    result = []
    queue = []
    visit = [0]*n
    for i in range(n):
        if matrix[i][0] == s:
            visit[i] = 1
            queue.append(i)
            while len(queue) > 0:
                cur = queue.pop(0)
                result.append(cur)
                for j in range(1, n+1):
                    if matrix[cur][j] == "1" and visit[j-1] == 0:
                        queue.append(j-1)
                        visit[j-1] = 1
                    else:
                        continue
    fun = lambda x: node[x]
    print(" ".join(list(map(fun, result))))


if __name__ == '__main__':
    # n = 4
    # s = 'a'
    # nodes =['a','b','c','d']
    # matrix = [['a','0','1','1','0'],['b','1','0','1','0'],
    #           ['c','1','1','0','1'],['d','0','0','1','0']]
    # bfs(matrix,s,n, nodes)
    n = int(input())
    for i in range(n):
        info = [x for x in input().split(' ')]
        size = int(info[0])
        start = info[1]
        node = [x for x in input().split(' ')]
        matrix = []
        for _ in range(size):
            temp = list(input().split(' '))
            matrix.append(temp)
        # print(matrix)
        bfs(matrix, start, size, node)


