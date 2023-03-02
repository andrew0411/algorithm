import sys
from collections import deque
import copy

input = sys.stdin.readline

'''
입력
- 그래프의 크기 N
- 그래프 정보

출력
- 검은 방에서 흰방으로 바꾸어야할 최소의 수
'''

N = int(input())
graph = [ list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [ [ -1 for _ in range(N)] for _ in range(N)]
s_x, s_y = 0, 0
e_x, e_y = N - 1, N - 1

def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    visited[start_x][start_y] = 0

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        u, v = queue.popleft()
        if u == e_x and v == e_y:
            return visited[u][v]
        
        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]
            if 0 <= new_u < N and 0 <= new_v < N:
                if visited[new_u][new_v] == -1:
                    if graph[new_u][new_v] == 0:
                        queue.append([new_u, new_v])
                        visited[new_u][new_v] = visited[u][v] + 1

                    else:
                        queue.appendleft([new_u, new_v])
                        visited[new_u][new_v] = visited[u][v]

print(bfs(s_x, s_y))