import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
m = int(input().rstrip())

'''
아이디어

1. 전체 bfs 한다음에 상근이와의 거리가 1 또는 2인 친구들 count
'''

graph = [[] for i in range(N + 1)]
visited = [-1 for i in range(N + 1)]

for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 0

    while queue:
        u = queue.popleft()
        
        for v in graph[u]:
            if visited[v] == -1:
                visited[v] = visited[u] + 1
                queue.append(v)

    return sum([x == 1 or x == 2 for x in visited])
    
start = 1
result = bfs(start)
print(result)