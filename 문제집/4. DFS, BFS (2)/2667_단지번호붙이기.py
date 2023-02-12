import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

1. 전체 원소에 대해 bfs 수행
2. visited 처리를 해줄 수 있는 flag를 하나 설정
3. 메모리 효율적으로 visited 딱히 필요 없게
'''

N = int(input().rstrip())

graph = [ list(map(int, list(input().rstrip()))) for _ in range(N)]
flag = 2
result = []

def bfs(x, y):
    global flag

    queue = deque()
    queue.append([x, y])
    graph[x][y] = flag
    temp = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        u, v = queue.popleft()
        for i in range(4):
            new_u, new_v = u + dx[i], v + dy[i]
            if 0 <= new_u < N and 0 <= new_v < N:
                if graph[new_u][new_v] == 1:
                    queue.append([new_u, new_v])
                    graph[new_u][new_v] = flag
                    temp += 1
    flag += 1
    result.append(temp)




for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)

print(len(result))
print(*sorted(result), sep='\n')