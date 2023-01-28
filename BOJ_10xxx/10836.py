import sys


M, N = map(int, sys.stdin.readline().split())

result = [1] * (2*M-1)
grow_arr = [0] * (2*M-1)

for i in range(N):
    zero, one, two = map(int, sys.stdin.readline().split())

    for i in range(zero, zero + one):
        grow_arr[i] += 1
    for i in range(zero + one, 2 * M - 1):
        grow_arr[i] += 2

result = list(map(lambda x, y : x + y, result, grow_arr))
repeat = result[-M+1:]
for i in range(M):
    print(result[M-1-i], *repeat)