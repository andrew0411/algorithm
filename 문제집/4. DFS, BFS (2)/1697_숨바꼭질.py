import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

MAX_GRAPH_SIZE = 100001

'''
아이디어

움직일수있는 방향벡터가 +1, -1, 또는 2*x
'''

graph = [-1 for i in range(MAX_GRAPH_SIZE)]

def bfs(s):
    queue = deque()
    queue.append(s)

    graph[s] = 0

    while queue:
        u = queue.popleft()

        if u == K:
            return graph[K]

        for new_u in [u - 1, u + 1, u * 2]:
            if 0 <= new_u < MAX_GRAPH_SIZE:
                if graph[new_u] == -1:
                    queue.append(new_u)
                    graph[new_u] = graph[u] + 1


start = N
result = bfs(start)
print(result)