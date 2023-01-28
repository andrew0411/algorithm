import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))
T.sort(reverse=True)

MAX = 0
for i in range(N):
    MAX = max(MAX, T[i] + i + 1)
print(MAX + 1)