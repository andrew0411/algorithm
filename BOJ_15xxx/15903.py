import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

card = list(map(int, input().split()))

heapq.heapify(card)

for i in range(m):
    t1 = heapq.heappop(card)
    t2 = heapq.heappop(card)
    temp = t1 + t2
    heapq.heappush(card, temp)
    heapq.heappush(card, temp)

print(sum(card))