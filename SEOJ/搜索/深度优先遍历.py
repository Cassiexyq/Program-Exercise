# -*- coding: utf-8 -*-

"""
@Time    : 2019/2/26 13:41
@Author  : Cassie
@Description :
"""


def dfs(matrix, start, depth):
    global max_depth
    global v
    if depth > max_depth:
        max_depth = depth

    for i in matrix[start]:
        if i not in v:
            v.append(i)
            dfs(matrix, i, depth+1)
            v.pop()


if __name__ == '__main__':
    # n = 4
    # s = 'd'
    # nodes =['a','b','c','d']
    # matrix = [['a','0','1','1','0'],['b','1','0','1','0'],
    #           ['c','1','1','0','1'],['d','0','0','1','0']]
    # dfs(matrix,s,n, nodes)

    case = int(input())
    for i in range(case):
        v = []
        max_depth = -1
        vertexNum, start = input().split(' ')
        num = int(vertexNum)
        graph = {}  # 把输入的邻接矩阵存入字典，存入的是顶点信息
        nodes = input().split(' ')
        for node in nodes:
            graph[node] = []
        for i in range(num):
            temp = input().split(' ')
            for j in range(num):
                if temp[j+1] == '1':
                    graph[temp[0]].append(nodes[j])
        print(graph)
        v.append(start)
        dfs(graph,start,1)
        print(max_depth)
