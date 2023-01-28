N, k = map(int, input().split())
coins = [0] * N
for i in range(N):
    coins[i] = int(input())
result = 0

for i in range(N):
    if k >= coins[N-1-i]:
        result += k // coins[N-1-i]
        k = k % coins[N-1-i]
print(result)