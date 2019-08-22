# -*- coding: utf-8 -*-

# @Author: xyq



from collections import defaultdict, deque
N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)
queue = deque()
queue.append((1, 0))
visit = set([1])
max_depth = 0
while queue:
    node, depth = queue.popleft()
    max_depth = max(depth, max_depth)
    for child in graph[node]:
        if child not in visit:
            visit.add(child)
            queue.append((child, depth+1))
print(visit)
print(queue)
print(2*(N-1)-max_depth)