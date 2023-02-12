import sys
from collections import deque
import copy

input = sys.stdin.readline

N = int(input().rstrip())
ref_graph = [ list(map(int, list(input().rstrip().split()))) for _ in range(N) ]

MAX_land = 0
MAX_H = max(map(max, ref_graph))

def bfs(height, x, y, graph):
    if graph[x][y] <= height:
        return False

    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        u, v = queue.popleft()
        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]
            if 0 <= new_u < N and 0<= new_v < N:
                if graph[new_u][new_v] > h:
                    queue.append([new_u, new_v])
                    graph[new_u][new_v] = 0

    return True

for h in range(MAX_H + 1):
    g = copy.deepcopy(ref_graph)
    temp = 0
    for i in range(N):
        for j in range(N):
            if bfs(h, i, j, g):
                temp += 1
                
    if temp > MAX_land:
        MAX_land = temp

print(MAX_land)