n = int(input())

n_rec = 0
n_dp = 0

def rec(n):
    global n_rec
    if n == 1 or n == 2:
        n_rec += 1
        return 1
    else:
        return rec(n - 1) + rec(n - 2)

dp_list = [1, 1]
def dp(n):
    global n_dp
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n - 2):
            n_dp += 1
            dp_list.append(dp_list[i] + dp_list[i + 1])

        return dp_list[n - 1]
    
rec(n)
dp(n)

print(n_rec, n_dp)