# BFS

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

visited = [-1] * (N + 1)

cnt = 0

for i in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

def bfs(position):
    queue = deque([position])
    visited[position] = 0
    while queue:
        node = queue.popleft()

        for child in graph[node]:
            if visited[child] == -1:
                visited[child] = 0
                queue.append(child)

    return 0

for i in range(1, N + 1):
    if visited[i] == -1:
        cnt += 1
        bfs(i)

print(cnt)