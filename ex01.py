import sys

input = sys.stdin.readline

M = int(input())
N = int(input())

result = []

def isSquare(x):
    print(int(x**(1/2))**2)

for i in range(M, N + 1):
    isSquare(i)