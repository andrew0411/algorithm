import sys
input = sys.stdin.readline

N = int(input())
Ns = [0] * N
for i in range(N):
    Ns[i] = int(input())
print(*sorted(Ns))

'''
short coding

print(*sorted(map(int,[*open(0)][1:])))
'''