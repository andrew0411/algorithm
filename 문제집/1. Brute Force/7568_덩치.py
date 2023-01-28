import sys

input = sys.stdin.readline

N = int(input())
arr = []
result = [1 for _ in range(N)]

for i in range(N):
    w, h = map(int, input().split())
    arr.append((w, h))

for i in range(N):
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            result[i] += 1

print(*result)