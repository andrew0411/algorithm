import sys
from collections import deque
input = sys.stdin.readline

'''
아이디어

1. 점프할때 + 1, 즉 거리 계산
'''

N = int(input().rstrip())
graph = list(map(int, input().rstrip().split()))
visited = [-1 for _ in range(N)]

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 0

    while queue:
        u = queue.popleft()

        for jump in range(1, graph[u] + 1):
            if u + jump <= N - 1:
                if visited[u + jump] == -1:
                    queue.append(u + jump)
                    visited[u + jump] = visited[u] + 1

start = 0
end = N - 1
bfs(start)
print(visited[end])