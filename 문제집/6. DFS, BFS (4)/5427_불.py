import sys
from collections import deque
import copy
from itertools import combinations


input = sys.stdin.readline

'''
입력
- 테스트 케이스의 개수 T
- 빌딩지도의 너비와 높이 w, h
- 빌딩지도의 정보

출력
- 빌딩을 탈출하는데 걸리는 시간

조건
- '.' 빈 공간, '#' 벽, '@' 시작 위치, '*' 불

1트
- 이동한다음에 그 장소로 불이 옮겨 붙는 경우를 고려못했음.
- 그래서 불이 먼저 번지는 걸로 구현해서 해결.
'''

T = int(input())

result = []

def bfs(s_x, s_y, fire_queue):
    queue = deque()
    queue.append([s_x, s_y])
    visited[s_x][s_y] = 0

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        for _ in range(len(fire_queue)):
            u, v = fire_queue.popleft()
            for i in range(4):
                new_u, new_v = u + dx[i], v + dy[i]
                if 0 <= new_u < H and 0 <= new_v < W:
                    if graph[new_u][new_v] == '.':
                        graph[new_u][new_v] = '*'
                        fire_queue.append([new_u, new_v])

        for _ in range(len(queue)):
            u, v = queue.popleft()
            for i in range(4):
                new_u, new_v = u + dx[i], v + dy[i]
                if 0 <= new_u < H and 0 <= new_v < W:
                    if visited[new_u][new_v] == -1:
                        if graph[new_u][new_v] == '.':
                            visited[new_u][new_v] = visited[u][v] + 1
                            queue.append([new_u, new_v])
                else:
                    return visited[u][v] + 1


    return 'IMPOSSIBLE'



for _ in range(T):
    W, H = map(int, input().split())
    graph = [ list(input().rstrip()) for _ in range(H)]
    visited = [ [-1] * W for _ in range(H) ]
    fire = [ [-1] * W for _ in range(H) ]
    fire_queue = deque()
    for h in range(H):
        for w in range(W):
            if graph[h][w] == '@':
                start_x = h
                start_y = w
            if graph[h][w] == '*':
                fire_queue.append([h, w])

    result.append(bfs(start_x, start_y, fire_queue))

print(*result, sep='\n')