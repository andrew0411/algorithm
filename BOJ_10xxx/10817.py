import sys

input = sys.stdin.readline
ls = list(map(int,input().split()))
print(sorted(ls)[1])