import sys
from collections import deque
import copy

input = sys.stdin.readline

'''
입력
- 트리의 노드 개수 N
- 0번줄부터 N-1번줄까지 각 노드의 부모
- 지울 노드

출력
- 리프 노드(자식의 개수가 0인 노드)의 개수

조건
- 부모가 없는 노드는 -1

아이디어
- 리프노드 편하게 계산하려면 자기 바로 밑의 자식을 포함하도록 그래프 생성
'''

N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
graph = [[] for _ in range(N)]

visited = [-1] * N
for i in range(N):
    if parents[i] == -1:
        continue
    i_parent = parents[i]
    graph[parents[i]].append(i)

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 0
    for i in range(N): # 지워질 노드를 자식으로 가지고 있는 부모에게서도 지워줌
        if node in graph[i]:
            graph[i].remove(node)

    while queue:
        u = queue.popleft()

        for child in graph[u]:
            queue.append(child)
            visited[child] = 0

bfs(del_node)

cnt = 0
for i in range(N):
    if visited[i] == -1 and not graph[i]:
        cnt += 1

print(cnt)