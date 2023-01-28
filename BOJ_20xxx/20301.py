import sys
from collections import deque

input = sys.stdin.readline

N, K, M = map(int, input().split())

result = []

nums = deque([i for i in range(1, N + 1)])

cnt = 0

while nums:
    if cnt == M:
        nums.reverse()
        cnt = 0

    nums.rotate(-K+1)
    result.append(nums.popleft())
    cnt += 1

print(*result, sep='\n')