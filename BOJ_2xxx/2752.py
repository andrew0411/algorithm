import sys
input = sys.stdin.readline

N = list(map(int, input().split()))
print(*sorted(N))

'''
short coding

print(*sorted(input().split(),key=int))
'''