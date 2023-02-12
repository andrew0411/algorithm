import sys
from collections import deque
import copy

input = sys.stdin.readline

N = int(input().rstrip())

'''
아이디어

1. bfs 돌리면서 영역 개수 세고, 그중 가장 큰 거 update

2. bfs 안에서 h 값으로 판별 + h보다 크면 모두 0으로
'''

ref_graph = [ list(map(int, list(input().rstrip().split()))) for _ in range(N)]

def bfs(s_x, s_y, graph, h):

    if graph[s_x][s_y] <= h:
        return False
    
    queue = deque()
    queue.append([s_x, s_y])
    graph[s_x][s_y] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        u, v = queue.popleft()
        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]

            if 0 <= new_u < N and 0 <= new_v < N:
                if graph[new_u][new_v] > h:
                    graph[new_u][new_v] = 0
                    queue.append([new_u, new_v])

    return True

result = []
for h in range(101):
    graph = copy.deepcopy(ref_graph)
    temp_result = 0
    for i in range(N):
        for j in range(N):
            if bfs(i, j, graph, h):
                temp_result += 1

    result.append(temp_result)

print(max(result))