# 인접 그래프 + DFS (1)

import sys

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

graph = [[] for i in range(N + 1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())

    graph[x].append(y)
    graph[y].append(x)

visited = []

def dfs(position):
    visited.append(position) 
    if graph[position]:
        for i in graph[position]:
            if i not in visited:
                dfs(i)


dfs(1)

# 1번은 이미 걸려 있기 때문에 -1
print(len(visited) - 1)