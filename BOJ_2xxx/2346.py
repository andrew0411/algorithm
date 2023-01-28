import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

result = []
nums = list(map(int, input().split()))
balloon = deque([(i, nums[i - 1]) for i in range(1, n + 1)])

while True:
    if not balloon:
        print(*result)
        break
    else:
        t = balloon.popleft()
        result.append(t[0])
        if t[1] > 0:
            balloon.rotate(-t[1]+1)
        else:
            balloon.rotate(-t[1])