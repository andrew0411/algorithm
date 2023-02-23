import sys
from collections import deque

input = sys.stdin.readline

'''
입력
- 그래프 크기 : M(가로), N(세로), H(높이)
- 토마토의 정보 : N x H 개 (각 줄에는 M개에 대한 정보)

출력
- 토마토가 모두 익을 수 없다면 -1
- 토마토가 모두 익어 있다면 0
- 토마토가 익는데까지 걸리는 시간

조건
- 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 6방향 고려
- 하루에 한번만 익음
- 토마토 정보 : 0(안익음), 1(익음), -1(토마토 없음)

아이디어
- 그냥 bfs 쭉 구현해서 MAX 값 추출
'''

M, N, H = map(int, input().split())

### 그래프 생성
graph = []
tomato_pos = [] # 입력으로 받은 익은 토마토의 정보
for h in range(H):
    temp = []
    for n in range(N):
        info = list(map(int, input().split()))
        temp.append(info)
        for m in range(M):
            if info[m] == 1:
                tomato_pos.append([h, n, m])
    graph.append(temp)

### Queue 미리 만들기
visited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
for x, y, z in tomato_pos:
    visited[x][y][z] = 0

# BFS 구성 : 탐색을 한번만 하게 하기 위해 for _ in range(len(queue))
def bfs(tomato_pos):
    queue = deque(tomato_pos)
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    MAX = 0
    while queue:
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            for i in range(6):
                new_x, new_y, new_z = x + dx[i], y + dy[i], z + dz[i]
                if 0 <= new_x < H and 0 <= new_y < N and 0 <= new_z < M:
                    if graph[new_x][new_y][new_z] == 0:
                        if visited[new_x][new_y][new_z] == -1:
                            queue.append([new_x, new_y, new_z])
                            visited[new_x][new_y][new_z] = visited[x][y][z] + 1
                            graph[new_x][new_y][new_z] = 1
                            MAX = max(MAX, visited[x][y][z] + 1)
    
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    return -1

    return MAX

print(bfs(tomato_pos))