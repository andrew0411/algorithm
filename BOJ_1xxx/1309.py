import sys

si = sys.stdin.readline


N = int(si())

dp = [[0, 0, 0] for _ in range(N + 1)]

dp[1] = [1, 1, 1] # 왼쪽 / 오른쪽 / 선택 x

for i in range(2, N + 1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901

print(sum(dp[N]) % 9901)