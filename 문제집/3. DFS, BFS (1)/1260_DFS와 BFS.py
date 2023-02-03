import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0 for i in range(N + 1)] for j in range(N + 1)]

dfs_visited = []
bfs_visited = []

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(position):
    dfs_visited.append(position)

    for i in range(N + 1):
        if graph[position][i] and i not in dfs_visited:
            dfs(i)

    return dfs_visited


def bfs(position):
    queue = deque([position])

    bfs_visited.append(position)

    while queue:
        v = queue.popleft()
        for i in range(N + 1):
            if graph[v][i] and i not in bfs_visited:
                queue.append(i)
                bfs_visited.append(i)

    return bfs_visited

print(*dfs(V))
print(*bfs(V))