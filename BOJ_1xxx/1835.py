import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

result =  deque([])

n = N

while len(result) < N:
    result.appendleft(n)

    for i in range(n):
        result.appendleft(result.pop())
    
    n -= 1
    
print(*result)