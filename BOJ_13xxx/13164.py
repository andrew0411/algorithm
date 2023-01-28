import sys
input = sys.stdin.readline

N, k = map(int, input().split())
height = list(map(int, input().split()))
temp = []
for i in range(N-1):
    temp.append(height[i+1]-height[i])

print(sum(sorted(temp)[:N-k]))