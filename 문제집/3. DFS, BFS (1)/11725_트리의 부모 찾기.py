import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

1차
BFS를 수행하면서 visited 값에 부모 노드의 값을 넣어주면 되지 않을까?
'''

N = int(input().rstrip())

graph = [[] for i in range(N + 1)]
visited = [-1 for i in range(N + 1)]

for i in range(N - 1):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        node = queue.popleft()
        for u in graph[node]:
            if visited[u] == -1:
                queue.append(u)
                visited[u] = node

start = 1

bfs(start)

for i in range(2, N + 1):
    print(visited[i])
