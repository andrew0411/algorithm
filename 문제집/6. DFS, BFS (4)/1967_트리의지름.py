import sys
from collections import deque, defaultdict
import copy
from itertools import combinations


input = sys.stdin.readline
sys.setrecursionlimit(10**4)
'''
입력
- 노드의 개수 N
- N개의 간선 [부모노드, 자식노드, 간선의 가중치]

출력
- 트리의 지름

조건
- 부모 노드는 항상 1
- 트리의 지름은 경로들 중 가장 긴 것

1트

v in visited 이거 하면 for 문 돌리는 거랑 같다고 했었음.

2트

시간 초과 시발 
'''

N = int(input())
edge_info = [ list(map(int, input().split())) for _ in range(N - 1)]
root = 1

def find_diameter(edges, root):
    tree = defaultdict(list)
    for parent, child, weight in edges:
        tree[parent].append([child, weight]) # 트리 dictionary 생성
        tree[child].append([parent, weight])

    def bfs(start):
        max_dist = 0
        far_node = None

        visited = set()
        visited.add(start)
        queue = deque()
        queue.append([start, 0])

        while queue:
            node, distance = queue.popleft()
            
            if distance > max_dist:
                max_dist = distance
                far_node = node

            for child, weight in tree[node]:
                if child not in visited:
                    queue.append([child, distance + weight])
                    visited.add(child)

        return max_dist, far_node
            
    _, far_node = bfs(root)
    diameter, _ = bfs(far_node)
    return diameter
    
print(find_diameter(edge_info, root))