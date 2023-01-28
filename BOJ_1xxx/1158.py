import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

result = []

ppl = deque()

for i in range(1,  n + 1):
    ppl.append(i)

for i in range(n):
    ppl.rotate(-k+1)
    result.append(ppl.popleft())
result = str(result).strip('[').rstrip(']')
print('<'+result+'>')