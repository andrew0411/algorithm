def get_num_infect(n):
    dp = [1, 1]
    for i in range(n - 2):
        dp.append(dp[i] + dp[i + 1])

    return dp[n - 1]
    
while True:
    n = int(input())
    if n == -1:
        break
    print(f'Hour {n}: {get_num_infect(n)} cow(s) affected')