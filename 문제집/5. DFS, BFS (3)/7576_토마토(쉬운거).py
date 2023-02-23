import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
tomato_pos = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato_pos.append([i, j])
            visited[i][j] = 0


def bfs():
    queue = deque(tomato_pos)
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    MAX = 0

    while queue:
        for _ in range(len(queue)):
            u, v = queue.popleft()
            for i in range(4):
                new_u, new_v = u + dx[i], v + dy[i]
                if 0 <= new_u < N and 0 <= new_v < M:
                    if graph[new_u][new_v] == 0 and visited[new_u][new_v] == -1:
                        queue.append([new_u, new_v])
                        graph[new_u][new_v] = 1
                        visited[new_u][new_v] = visited[u][v] + 1
                        MAX = max(MAX, visited[u][v] + 1)

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1

    return MAX

print(bfs())