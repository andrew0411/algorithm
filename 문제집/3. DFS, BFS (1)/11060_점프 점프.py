import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

최소 점프이므로, visited에 원래 있던 값과 비교해서 작은 값을 넣어주면 됨

또한 점프할 수 있는 칸의 크기가 N으로 제한되어있어서 칸을 넘는지 조사해줘야댐
'''

N = int(input().strip())
graph = list(map(int, input().rstrip().split()))
visited = [-1 for i in range(N)]

start = 0
end = N - 1

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        node = queue.popleft()
        if node == end:
            return visited[end]

        for i in range(node + 1, node + graph[node] + 1):
            if i <= N - 1:
                if visited[i] == -1:
                    visited[i] = visited[node] + 1
                    queue.append(i)

    return visited[end]

print(bfs(start))