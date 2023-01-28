import sys
from collections import deque

k = int(input())
arr = deque()

for i in range(k):
    t = int(input())
    
    if t == 0:
        arr.pop()
    else:
        arr.append(t)

print(sum(arr))