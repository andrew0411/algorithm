import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

1. start부터 end까지 갈때 얼마나 걸리는가
'''

N, M = map(int, input().rstrip().split())
graph = [ list(map(int, list(input().rstrip()))) for _ in range(N) ]
visited = [ [-1 for _ in range(M)] for __ in range(N)]

s_x, s_y = 0, 0
e_x, e_y = N - 1, M - 1

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        u, v = queue.popleft()

        if u == e_x and v == e_y:
            return visited[u][v]

        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]
            if 0 <= new_u < N and 0 <= new_v < M:
                if graph[new_u][new_v] == 1:
                    if visited[new_u][new_v] == -1:
                        queue.append([new_u, new_v])
                        visited[new_u][new_v] = visited[u][v] + 1


result = bfs(s_x, s_y)

print(result)