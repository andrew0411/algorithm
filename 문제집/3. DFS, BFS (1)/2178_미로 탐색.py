import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

start = [0, 0]

end = [N - 1, M - 1]

graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]

'''
아이디어

(0, 0)에서 시작해서 모든 방향으로 탐색하는 BFS 실행.

이동할 수 있는 칸이면서, 한번도 방문하지 않은 노드에 대해 (prior 값 + 1)을 줌

'''

visited  = [[-1 for i in range(M)] for j in range(N)]

def bfs(start):
    x, y = start
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        u, v = queue.popleft()

        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]

            if 0 <= new_u < N and 0 <= new_v < M:
                if graph[new_u][new_v] == 1 and visited[new_u][new_v] == -1:
                    visited[new_u][new_v] = visited[u][v] + 1
                    queue.append([new_u, new_v])


    end_x, end_y = end
    return visited[end_x][end_y]

print(bfs(start))