M = int(input())
N = int(input())

def isSquare(n):
    return (n ** 0.5) % 1 == 0

SUM = 0
minimum = N+100
for i in range(M, N+1):
    if isSquare(i):
        SUM += i
        if i < minimum:
            minimum = i
if SUM == 0:
    print(-1)
else:
    print(SUM)
    print(minimum)