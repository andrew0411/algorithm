import sys

input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()


def lcs(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:  # 문자가 같을 때
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 문자가 다를 때
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


print(lcs(str1, str2))
