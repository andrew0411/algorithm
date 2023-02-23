import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

'''
입력
- 그래프 크기 N, M
- 그래프 정보 0(빈칸), 1(벽), 2(바이러스의 위치)

출력
- 안전영역 크기의 최댓값

조건
- 바이러스는 상하좌우로 퍼져나감
- 안전영역의 크기가 최대가 되도록 벽을 3개 세워야 함

아이디어
- 지도에서 0인 부분의 좌표에서 3개를 무작위로 골라서 bfs 반복 수행 (시간초과날거같은데 ㅅㅂ)
'''

N, M = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(N)]
zeros = []
viruses = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zeros.append([i, j])
        if graph[i][j] == 2:
            viruses.append([i, j])

MAX = 0

def count(graph):
    SUM = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                SUM += 1

    return SUM

def bfs(s_x, s_y, graph):
    queue = deque()
    queue.append([s_x, s_y])

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        u, v = queue.popleft()
        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]
            if 0 <= new_u < N and 0 <= new_v < M:
                if graph[new_u][new_v] == 0:
                    queue.append([new_u, new_v])
                    graph[new_u][new_v] = 2

for temp in combinations(zeros, 3):
    g = copy.deepcopy(graph)
    for i in temp:
        g[i[0]][i[1]] = 1

    for i, j in viruses:
        bfs(i, j, g)

    MAX = max(MAX, count(g))

print(MAX)