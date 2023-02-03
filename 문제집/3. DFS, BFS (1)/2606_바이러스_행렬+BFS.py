# 인접 행렬 + BFS (4)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for i in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1 for _ in range(N + 1)]

def bfs():
    queue = deque([1])
    visited[1] = 0
    while queue:
        node = queue.popleft()
        if graph[node]:
            for u in graph[node]:
                if visited[u] == -1:
                    queue.append(u)
                    visited[u] = 0

    return visited

print(N + sum(bfs()))