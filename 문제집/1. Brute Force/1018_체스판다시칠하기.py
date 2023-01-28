import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [input().strip() for _ in range(N)]

s1 = 'WB' * 4
s2 = 'BW' * 4
ref1 = [s1, s2] * 4
ref2 = [s2, s1] * 4

result = 32

for i in range(N - 7):
    for j in range(M - 7):
        temp = [x[j : j + 8] for x in arr[i : i + 8]]
        
        new1 = sum([ref1[i][j] == temp[i][j] for j in range(8) for i in range(8)])
        new2 = sum([ref2[i][j] == temp[i][j] for j in range(8) for i in range(8)])

        new = min(new1, new2)

        if new < result:
            result = new

print(result)