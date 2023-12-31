n = int(input())

dp = [0, 1]

if n >= 2:
    for i in range(n - 1):
        dp.append(dp[i] + dp [i + 1])

print(dp[n])