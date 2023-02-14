import sys
from collections import deque

input = sys.stdin.readline

'''
입력      
- 그래프의 크기, 직사각형 개수
- 직사각형의 왼쪽 아래 (x, y)와 오른쪽 위 (x, y)
        
출력
- 분리된 영역의 개수, sorted(분리된 영역의 각 넓이)

아이디어
- 0. 그래프를 모두 1로 초기화
- 1. 직사각형의 좌표 두개를 받아서 graph 상에 0으로 채우기
- 2. 전체 좌표를 돌면서 1인 경우에 bfs 수행 및 개수 세기
- 3. 모눈종이의 왼쪽 아래가 (0, 0) 이든 왼쪽 위가 (0, 0)이든 아무 상관없음
'''

## 입력 및 그래프 생성

M, N, K = map(int, input().rstrip().split())
graph = [[1 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    l_x, l_y, r_x, r_y = map(int, input().rstrip().split())
    for i in range(r_x - l_x):
        for j in range(r_y - l_y):
            new_x, new_y = l_x + i, l_y + j
            graph[new_y][new_x] = 0


## BFS 구현
def bfs(x, y):

    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0
    cnt = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        u, v = queue.popleft()
        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]
            if 0 <= new_u < M and 0 <= new_v < N:
                if graph[new_u][new_v] == 1:
                    queue.append([new_u, new_v])
                    graph[new_u][new_v] = 0
                    cnt += 1
    
    return cnt

## 출력
result = []
count = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(i, j))
            count += 1


print(count)
print(*sorted(result))