import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

'''

입력      
- 그래프 크기 10 x 10 (제일 왼쪽 아래가 1)
- N개의 사다리 좌표, M개의 뱀 좌표
- BFS 횟수 S, 탐색할 위치 (x, y)
        
출력
- END에 도착하는데 걸리는 횟수

조건
- 주사위를 던짐 (1~6 이동)
- queue에 현재위치, 시간 넣어줌
- 사다리랑 뱀은 시작점과 끝점이 있는, 즉 유향 엣지임.

[2트]
방문했던 점이 queue에 계속 들어가서 그럼.
방문처리를 왜 안해줬을까 ㅅㅂ
'''
N, M = map(int, input().split())
start = 1
end = 100
graph = [[] for _ in range(101)]
visited = [-1 for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    graph[x].append(y)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
# 사다리와 뱀 정보 

def bfs(start):
    queue = deque()
    queue.append([start, 0])
    visited[start] = 0
    dx = [1, 2, 3, 4, 5, 6]

    while queue:
        node, time = queue.popleft()
        if node == end:
            return time
        for d in dx:
            new_node = node + d
            if new_node <= 100:
                if visited[new_node] == -1:
                    if graph[new_node]:
                        queue.append([graph[new_node][0], time + 1])
                        visited[new_node] = 0
                    else:
                        queue.append([new_node, time + 1])
                        visited[new_node] = 0

print(bfs(start))