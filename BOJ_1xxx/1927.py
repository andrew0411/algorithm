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
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, x)
print(*result, sep='\n')