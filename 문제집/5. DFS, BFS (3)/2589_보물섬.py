import sys
from collections import deque
import copy

input = sys.stdin.readline

'''
입력
- 그래프의 크기 H, W
- 보물지도 : L(육지), W(바다)

조건
- 육지로만 이동해야됨
- 연결되어있는 육지 중에서 max(min(x1, x2)) 찾아야함

출력
- 최단 시간

아이디어
[1트] 시간초과
- 메모리 넉넉하니깐 그냥 visited
'''

H, W = map(int, input().split())
graph = [ input().rstrip() for _ in range(H)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



def bfs(xi, xj):
    queue = deque()
    visited = [[-1 for _ in range(W)] for _ in range(H)]
    queue.append([xi, xj])
    visited[xi][xj] = 0
    temp = -1
    
    while queue:
        size = len(queue)
        for _ in range(size):
            u, v = queue.popleft()
            for i in range(4):
                new_u, new_v = u + dx[i], v + dy[i]
                if 0 <= new_u < H and 0 <= new_v < W:
                    if graph[new_u][new_v] == 'L':
                        if visited[new_u][new_v] == -1:
                            queue.append([new_u, new_v])
                            visited[new_u][new_v] = 0
        temp += 1

    return temp

MAX_D = 0
for i in range(H):
    for j in range(W):
        if graph[i][j] == 'L':    
            MAX_D = max(MAX_D, bfs(i, j))
print(MAX_D)