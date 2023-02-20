import sys
from collections import deque
import copy

input = sys.stdin.readline

'''
입력
- 총 건물높이 : F, 출발지 : S, 목적지 :G
- 이동 벡터 : 위로 U, 밑으로 D

출력
- S -> G 까지 최소로 가는 경우
- 갈 수 없으면 'use the stairs'

[2트] - 시간 초과
visited를 list에서 set으로 바꾸니깐 해결됨
'''

F, S, G, U, D = map(int, input().split())

def dfs(start):
    queue = deque()
    queue.append([start, 0])
    visited = set([start])

    while queue:
        node, cnt = queue.popleft()
        if node == G:
            return cnt
        for next_node in [node + U, node - D]:
            if 1 <= next_node <= F:
                if next_node not in visited:
                    queue.append([next_node, cnt + 1])
                    visited.add(next_node)

    return 'use the stairs'

result = dfs(S)
print(result)