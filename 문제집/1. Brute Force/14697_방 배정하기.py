import sys

input = sys.stdin.readline

A, B, C, N = map(int, input().split())

arr = [0 for _ in range(351)]

arr[A] = arr[B] = arr[C] = 1

for i in range(301):
    if arr[i] != 0:
        arr[i + A] = arr[i + B] = arr[i + C] = 1

print(arr[N])