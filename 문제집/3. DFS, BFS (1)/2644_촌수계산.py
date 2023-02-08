import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

1차
촌수를 계산해야하는 서로 다른 두사람의 사이의 거리를 계산하는 문제라고 생각할 수 있겠다

start, end를 사용하고, bfs() 돌리면서 end일때의 값을 찾으면 되겠다

2차 (start랑 end랑 아예 연결이 없어서 if node == end를 사용할 수 없는 경우)

-> while 문 밖에 return 하나더 추가
'''

n = int(input().rstrip())

graph = [[] for i in range(n + 1)]

visited = [-1 for i in range(n + 1)]

start, end = map(int, input().rstrip().split())

m = int(input().rstrip())

for i in range(m):
    u, v= map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        node = queue.popleft()
        if node == end:
            return visited[node]

        for u in graph[node]:
            if visited[u] == -1:
                queue.append(u)
                visited[u] = visited[node] + 1

    
    return visited[end]

print(bfs(start))