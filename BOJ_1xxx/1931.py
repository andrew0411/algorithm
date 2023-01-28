N = int(input())
time = []
for i in range(N):
    time.append(list(map(int, input().split())))
time.sort(reverse=True)
result = 0
refe = 2**32 -1
for t in time:
    if t[1] <= refe:
        result += 1
        refe = t[0]
print(result)