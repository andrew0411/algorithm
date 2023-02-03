# 인접 행렬 + DFS (2)

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())

    graph[u][v] = graph[v][u] = 1

visited = []

def dfs(position):
    visited.append(position)

    for i in range(N + 1):
        if graph[position][i] and i not in visited:
            dfs(i)

    return visited

print(len(dfs(1)) - 1)