import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

나이트가 이동할 수 있는 방법은 총 8가지

이때, 나이트가 end 지점에 다다르면 bfs를 종료하고 값을 반환하도록

또한 그 전 단계에서의 이동수 + 1을 bfs에서 수행
'''
def bfs(x, y, end_x, end_y):
    queue = deque()
    queue.append([x, y])
    
    graph[x][y] = 0

    du = [1, 1, 2, 2, -1, -1, -2, -2]
    dv = [2, -2, 1, -1, 2, -2, 1, -1]

    while queue:
        u, v = queue.popleft()
        if u == end_x and v == end_y:
            return graph[u][v]

        for i in range(8):
            new_x, new_y = u + du[i], v + dv[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if graph[new_x][new_y] == 0:
                    graph[new_x][new_y] = graph[u][v] + 1
                    queue.append([new_x, new_y])

T = int(input())

result = []

for t in range(T):
    N = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    graph = [[0 for i in range(N)] for j in range(N)]

    result_t = bfs(start_x, start_y, end_x, end_y)
    result.append(result_t)

print(*result, sep='\n')