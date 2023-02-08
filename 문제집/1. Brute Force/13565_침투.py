import sys
from collections import deque

'''
아이디어

start를 위쪽, end를 아래쪽으로 생각하고, 아래쪽에 1이 있는지 없는지 판별하는 걸로

또 visited를 따로 만들지 않고
0 : 이동불가, 1 : 이동가능, 2 : 이동해서 전류 흐름 으로 
'''

input = sys.stdin.readline
M, N = map(int, input().rstrip().split())
graph = [ list(map(int, list(input().rstrip()))) for i in range(M) ]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 2

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        u, v = queue.popleft()
        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]
            if 0 <= new_u < M and 0 <= new_v < N:
                if graph[new_u][new_v] == 0:
                    queue.append([new_u, new_v])
                    graph[new_u][new_v] = 2

for i in range(N):
    if graph[0][i] == 0:
        bfs(0, i)

if 2 in graph[-1]:
    print('YES')
else:
    print('NO')