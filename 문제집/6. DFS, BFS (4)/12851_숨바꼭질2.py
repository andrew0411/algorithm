import sys
from collections import deque
import copy
from itertools import combinations


input = sys.stdin.readline

'''
입력
- 수빈이의 위치 N, 동생의 위치 K

출력
- 수빈이가 동생을 찾는 가장 빠른 시간
- 가장 빠른 시간으로 동생을 찾는 방법의 수

조건
- 걷기 : 1초 후 x-1, x+1, 순간이동 : 1초 후 2*x

아이디어
- 최단시간은 하는 것은 쉬운데, 경우의 수를 어떻게 찾지
- graph에 시간과 경우의 수 저장
'''
MAX = 100001
graph = [[-1, 0] for _ in range(MAX)]

start, end = map(int, input().split())

def bfs(start):
    queue = deque()
    queue.append(start)
    graph[start][0] = 0
    graph[start][1] = 1

    while queue:
        u = queue.popleft()
        
        for v in [u + 1, u - 1, u * 2]:
            if 0 <= v < MAX:
                if graph[v][0] == -1: # 첫방문이면
                    graph[v][0] = graph[u][0] + 1 # 시간 + 1
                    graph[v][1] = graph[u][1] # 경우의 수 
                    queue.append(v)

                elif graph[v][0] == graph[u][0] + 1: # 첫방문은 아니지만 최단시간 도착이면
                    graph[v][1] += graph[u][1] # 전 단계까지 가는 방법의 경우의 수 더하기


bfs(start)

print(*graph[end], sep='\n')