from math import factorial

def solve(N, M):
    return factorial(M) // (factorial(N) * factorial(M - N))

T = int(input())
 
for test in range(T):
    N, M = map(int, input().split())
    print(solve(N, M))