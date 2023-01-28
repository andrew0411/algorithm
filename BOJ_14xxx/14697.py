a, b, c, N = map(int, input().split())

dp = [0] * 301
dp[a], dp[b], dp[c] = 1, 1, 1

if N%a == 0 or N%b == 0 or N%c == 0:
    print(1)
else:
    for i in range(301):
        if dp[i-a] or dp[i-b] or dp[i-c]:
            dp[i] = 1
    print(dp[N])