import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

해당 문제에서는 노드에서 노드로 갈 때, 가로, 세로, 대각선을 고려해야함.

나머지는 군집의 개수를 세는 문제와 동일

visited를 따로 만들지 않고, 방문을 했으면 -1로 값을 바꿔줌
'''
result = []

def bfs(u, v):
    queue = deque()
    queue.append([u, v])
    graph[u][v] = -1
    
    while queue:
        x, y = queue.popleft()

        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [0, 1, -1, 1, -1, 0, 1, -1]

        for i in range(8):
            new_x, new_y = x + dx[i], y + dy[i]

            if 0 <= new_x < h and 0 <= new_y < w:
                if graph[new_x][new_y] == 1:
                    queue.append([new_x, new_y])
                    graph[new_x][new_y] = -1


while True:

    w, h = map(int, input().rstrip().split())

    if w == 0 and h == 0:
        break
    
    result_t = 0

    graph = [list(map(int, input().rstrip().split())) for i in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                result_t += 1

    result.append(result_t)

print(*result, sep='\n')