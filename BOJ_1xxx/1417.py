import heapq
import sys

input = sys.stdin.readline

n = int(input())



dasom = int(input())
cnt = 0
if n == 1:
    print(0)

else:
    heap = []
    for i in range(n-1):
        heapq.heappush(heap, -int(input()))

    while True:
        if dasom > -heap[0]:
            print(cnt)
            break
        else:
            cnt += 1
            t = -heapq.heappop(heap)
            dasom += 1
            heapq.heappush(heap, -(t-1))