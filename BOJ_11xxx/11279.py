import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []
result = []

for i in range(N):
    x = int(input())
    if x == 0:
        if heap:
            result.append(heapq.heappop(heap)[1])
        else:
            result.append(0)
    else:
        heapq.heappush(heap, (-x, x))
print(*result, sep='\n')