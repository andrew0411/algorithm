import sys
from collections import deque
import copy
from itertools import combinations


input = sys.stdin.readline

'''
입력
- 노드 개수 N
- 구역의 인구
- 그래프 정보 

출력
- 두 선거구로 나누었을 때의 인구 차이의 최솟값
'''

N = int(input())
pop = list(map(int, input().split()))
MIN = 1000
graph = [ [] for _ in range(N + 1) ]

for i in range(N):
    temp = list(map(int, input().split()))
    for node in temp[1:]:
        graph[i + 1].append(node)

def bfs(nodes):
    queue = deque()
    queue.append(nodes[0])
    visited = [nodes[0]]
    temp = pop[nodes[0] - 1]
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited and v in nodes:
                queue.append(v)
                visited.append(v)
                temp += pop[v - 1]
    if len(visited) == len(nodes):
        return True, temp
    else:
        return False, temp


for i in range(1, int(N / 2) + 1):
    for comb in combinations(range(1, N + 1), i):
        part1 = comb
        part2 = tuple(set(range(1, N + 1)) - set(part1))
        check1, val1 = bfs(part1)
        check2, val2 = bfs(part2)
        if check1 and check2:
            MIN = min(MIN, abs(val1 - val2))

if MIN == 1000:
    print(-1)
else:
    print(MIN)
