import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

'''
입력      
- 테스트 케이스의 개수 t
- 편의점의 개수 n
- 출발지, 경유지, 도착지의 좌표 (x, y)
        
출력
- 조건을 만족하면서 도착가능 여부

아이디어
- 0. N + 2 개의 노드, 간선은 노드 사이의 길이인 그래프를 그린다
- 1. start 에서 end 까지 갈 수 있는지 연결성만 check
'''

T = int(input().rstrip())

def isConnect(x1, y1, x2, y2):
    length = abs(x1 - x2) + abs(y1 - y2)
    if length <= 1000:
        return True
    else:
        return False

def bfs(start, end, graph, visited):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        u = queue.popleft()
        if u == end:
            return 'happy'

        for v in graph[u]:
            if visited[v] == -1:
                queue.append(v)
                visited[v] = 0

    return 'sad'

result = []

for _ in range(T):
    n = int(input().rstrip())

    graph = [[] for _ in range(n + 2)]
    visited = [-1 for _ in range(n + 2)]

    s_x, s_y = map(int, input().rstrip().split())
    points = [[s_x, s_y]]
    for _ in range(n):
        x, y = map(int, input().rstrip().split())
        points.append([x, y])
    e_x, e_y = map(int, input().rstrip().split())
    points.append([e_x, e_y])

    for i, j in combinations(range(n + 2), 2):
        u, v = points[i], points[j]
        if isConnect(u[0], u[1], v[0], v[1]):
            graph[i].append(j)
            graph[j].append(i)

    ## 그래프 생성 완료
    start = 0
    end = n + 1
    result.append(bfs(start, end, graph, visited))
print(*result, sep='\n')