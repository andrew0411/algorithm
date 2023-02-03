# DFS

import sys
sys.setrecursionlimit(5000)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]

visited = [-1] * (N + 1)

cnt = 0

for i in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

def dfs(position):
    visited[position] = 0
    for i in graph[position]:
        if visited[i] == -1:
            dfs(i)

for i in range(1, N + 1):
    if visited[i] == -1:
        cnt += 1
        dfs(i)

print(cnt)