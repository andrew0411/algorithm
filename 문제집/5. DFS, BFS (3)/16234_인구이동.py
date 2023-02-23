import sys
from collections import deque

input = sys.stdin.readline

'''
입력
- 그래프 크기 : N, 인구 차이 L 이상, R 이하
- 각 나라의 인구수 N 개의 줄에서 N 씩 (그래프 만드는 입력)

출력
- 인구 이동이 발생하는 일 수

조건
- 서로 붙어 있는 나라가 조건 만족하면 인구 이동 시작
- 인구 이동이 되는 순간 (전체 인구수) / (나라 수) 가 됨 (소수점 버리니깐 int)

아이디어
- 1. 모든 점에 대해 bfs 수행해서 조건 만족하는지 check
- 2. 한 점과 조건 만족하는 모든 점들의 그래프 값 바꿔주기
'''
N, L, R = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(N)]

def bfs(s_x, s_y):
    global FLAG
    queue = deque()
    queue.append([s_x, s_y])
    visited[s_x][s_y] = 0
    temp = [[s_x, s_y, graph[s_x][s_y]]] # 인구 이동할 좌표, 값 저장
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        u, v = queue.popleft()
        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]
            if 0 <= new_u < N and 0 <= new_v < N and visited[new_u][new_v] == -1:
                if L <= abs(graph[u][v] - graph[new_u][new_v]) <= R:
                    temp.append([new_u, new_v, graph[new_u][new_v]])
                    queue.append([new_u, new_v])
                    visited[new_u][new_v] = 0

    if len(temp) != 1: # 국경이 하나 이상 열렸을 때만
        FLAG = True
        # 인구 이동 구현
        avg = int(sum([x[2] for x in temp]) / len(temp))
        for t in temp:
            graph[t[0]][t[1]] = avg


cnt = 0
FLAG = True
while FLAG:
    FLAG = False
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                bfs(i ,j)

    if FLAG:
        cnt += 1

print(cnt)