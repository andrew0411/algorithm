N = int(input())
k = [0] * N
for i in range(N):
    k[i] = int(input())
k.sort()
result = 0
for i in range(N):
    temp = k[i] * (N - i)
    if result < temp:
        result = temp
print(result)