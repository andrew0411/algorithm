import sys
input = sys.stdin.readline

N, k = map(int, input().split())
ls = list(map(int, input().split()))
print(sorted(ls)[-k])