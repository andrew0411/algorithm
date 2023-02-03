# 인접 그래프 + BFS (3)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[0 for i in range(N + 1)] for j in range(N + 1)]
visited = [False for i in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())

    graph[u][v] = graph[v][u] = 1


def bfs():
    queue = deque([1])

    while queue:
        node = queue.popleft()

        for i in range(N + 1):
            if graph[node][i] and not visited[i]:
                queue.append(i)
                visited[i] = True

    return visited

print(sum(bfs()) - 1)