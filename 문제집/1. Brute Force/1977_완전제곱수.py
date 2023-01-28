import sys

input = sys.stdin.readline

M = int(input())
N = int(input())

arr = []

def isSquare(x):
    if x == int(x**0.5)**2:
        return True
    else:
        return False

for i in range(M, N + 1):
    if isSquare(i):
        arr.append(i)

if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)