N = int(input())
p = list(map(int, input().split()))
p.sort()
result = 0
for i in range(N):
    result += (p[i] * (N-i))
print(result)