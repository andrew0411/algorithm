import sys
from collections import deque
import copy

input = sys.stdin.readline

'''
입력
- 그래프의 크기 : N
- 그래프 정보

출력
- 색약인 사람이 봤을 때의 구역 수 / 아닌 사람이 봤을 때 구역 수

조건
- 적녹색약은 B와 R을 같은 것으로 구분함

아이디어
- 구역 나누기 문제와 유사
- BFS 할때 정상인지 (False), 아닌지(True) FLAG 넣어주게 함
'''

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

rgb_visited = [[-1 for _ in range(N)] for _ in range(N)]
rg_visited = copy.deepcopy(rgb_visited)

def bfs(s_x, s_y, visited, FLAG):
    queue = deque()
    queue.append([s_x, s_y])
    visited[s_x][s_y] = 0
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        u, v = queue.popleft()
        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]
            if 0 <= new_u < N and 0 <= new_v < N:
                if visited[new_u][new_v] == -1:
                    if FLAG:
                        if graph[u][v] == 'R' or graph[u][v] == 'G':
                            if graph[new_u][new_v] == 'R' or graph[new_u][new_v] == 'G':
                                queue.append([new_u, new_v])
                                visited[new_u][new_v] = 0
                    
                    if graph[new_u][new_v] == graph[u][v]:
                        queue.append([new_u, new_v])
                        visited[new_u][new_v] = 0

rgb_cnt, rg_cnt = 0, 0

for i in range(N):
    for j in range(N):
        if rgb_visited[i][j] == -1:
            bfs(i, j, rgb_visited, False)
            rgb_cnt += 1
        
        if rg_visited[i][j] == -1:
            bfs(i, j, rg_visited, True)
            rg_cnt += 1

print(rgb_cnt, rg_cnt)