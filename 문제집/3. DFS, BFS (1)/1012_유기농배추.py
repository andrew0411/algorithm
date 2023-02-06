import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

(0, 0)부터 (N, M)까지 모든 노드를 start로 시작해서 

배추가 심어져있고(graph = 1) 한번도 방문하지 않았던 노드이면 +1 을 해줌
'''


T = int(input().rstrip())

result = []

def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    visited[start_x][start_y] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]

            if 0 <= new_x < N and 0 <= new_y < M:
                if graph[new_x][new_y] == 1:
                    if visited[new_x][new_y] == -1:
                        queue.append([new_x, new_y])
                        visited[new_x][new_y] = 0

for t in range(T):
    result_t = 0

    M, N, K = map(int, input().rstrip().split())

    graph = [[0 for i in range(M)] for j in range(N)]
    visited = [[-1 for i in range(M)] for j in range(N)]
    
    # 그래프 생성
    for k in range(K):
        v, u = map(int, input().rstrip().split())

        graph[u][v] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == -1:
                bfs(i, j)
                result_t += 1

    result.append(result_t)


print(*result, sep='\n')