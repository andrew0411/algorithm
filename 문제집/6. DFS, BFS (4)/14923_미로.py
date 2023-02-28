import sys
from collections import deque
import copy

input = sys.stdin.readline

'''
입력
- N, M 그래프 크기 (2 <= N <= 1000 and 2 <= M <= 1000)
- Hx, Hy 시작 위치
- Ex, Ey 도착 위치
- 그래프 정보 : 빈칸(0), 벽(1)

출력
- 가장 빠른 경로의 거리 D, 못가면 -1

조건
- 한번 벽 통과 가능

아이디어
- 지팡이 사용 flag를 queue랑 visited에 넣어주면 될 듯?
'''

N, M = map(int, input().split())
s_x, s_y = map(int, input().split())
e_x, e_y = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(N)]
visited = [ [ [-1, -1] for _ in range(M) ] for _ in range(N) ]

def bfs(start_x, start_y):
    queue = deque()
    FLAG = 0
    queue.append([start_x, start_y, FLAG])
    visited[start_x][start_y][FLAG] = 0

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    while queue:
        u, v, magic = queue.popleft()
        if u == e_x - 1 and v == e_y - 1:
            return visited[e_x - 1][e_y - 1][magic]

        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]
            if 0 <= new_u < N and 0 <= new_v < M:
                if visited[new_u][new_v][magic] == -1:
                    if magic == 0: # 마법 아직 안썼을 때
                        if graph[new_u][new_v] == 0: # 0은 그냥 지나감
                            queue.append([new_u, new_v, magic])
                            visited[new_u][new_v][magic] = visited[u][v][magic] + 1

                        if graph[new_u][new_v] == 1: # 1 만나면 뚫고 지나가고 flag 업데이트
                            queue.append([new_u, new_v, 1])
                            visited[new_u][new_v][1] = visited[u][v][magic] + 1

                    else:
                        if graph[new_u][new_v] == 0: # 마법 이미 썼으니깐 0 만 지나감
                            queue.append([new_u, new_v, magic])
                            visited[new_u][new_v][magic] = visited[u][v][magic] + 1

    return -1

print(bfs(s_x - 1, s_y - 1))