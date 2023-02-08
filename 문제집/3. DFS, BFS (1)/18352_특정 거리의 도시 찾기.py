import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

특정노드(출발도시)에서 거리가 K인 모든 노드를 출력하는 문제

1. visited에 거리 정보(start부터의 거리)를 넣는다

2. while 문 안에서 visited[node] 값이 K 이면 저장
'''

N, M, K, start = map(int, input().rstrip().split())
graph = [[] for i in range(N+ + 1)]
visited = [-1 for i in range(N + 1)]
result = []

for i in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        node = queue.popleft()

        if visited[node] == K:
            result.append(node)

        for u in graph[node]:
            if visited[u] == -1:
                queue.append(u)
                visited[u] = visited[node] + 1

bfs(start)

if result:
    print(*sorted(result), sep='\n')
else:
    print(-1)
