import sys

input = sys.stdin.readline

N = int(input())

result = 0

for i in range(N):
    s = str(i)
    if sum([int(x) for x in s]) + i == N:
        result = i
        break
print(result)