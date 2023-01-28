arr = [500, 100, 50, 10, 5, 1]

N = 1000 - int(input())
cnt = 0
for i in arr:
    cnt += N // i
    N %= i
print(cnt)