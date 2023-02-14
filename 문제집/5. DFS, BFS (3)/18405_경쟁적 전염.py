import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

'''
[1트]

입력      
- 그래프 크기 N, 바이러스 종류 K
- 그래프 정보 
- BFS 횟수 S, 탐색할 위치 (x, y)
        
출력
- 탐색할 위치에 존재하는 바이러스의 종류

조건
- 번호가 낮은 바이러스부터 증식
- 증식 방향은 상, 하, 좌, 우
- 바이러스가 존재하는 곳에는 바이러스가 들어갈 수 없음

아이디어
- 0. 번호가 낮은 바이러스부터 bfs를 수행
- 1. 1초에 증식 1번씩

[2트]
아이디어
0.  WC 일 때, 시간초과가 나기때문에 \
    바이러스의 종류와, 존재하는 위치, 현재 시간을 queue로 구성해주는 방법 사용
'''

N, K = map(int, input().split())

graph = []
pos = []
for i in range(N):
    g = list(map(int, input().split()))
    graph.append(g)
    for j in range(len(g)):
        if graph[i][j] != 0:
            pos.append([graph[i][j], i, j, 0])

S, END_x, END_y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque(sorted(pos))

while queue:
    k, x, y, t = queue.popleft()

    if t == S:
        break

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < N:
            if graph[new_x][new_y] == 0:
                graph[new_x][new_y] = k
                queue.append([k, new_x, new_y, t + 1])

print(graph[END_x - 1][END_y - 1])