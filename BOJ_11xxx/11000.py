import heapq
import sys


input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    s, t = map(int, input().split())
    heapq.heappush(heap, (s, t))

result = [heapq.heappop(heap)[1]]

while heap:
    cls = heapq.heappop(heap)
    start = heapq.heappop(result)

    if cls[0] < start:
        heapq.heappush(result, cls[1])
        heapq.heappush(result, start)
    else:
        heapq.heappush(result, cls[1])

print(len(result))