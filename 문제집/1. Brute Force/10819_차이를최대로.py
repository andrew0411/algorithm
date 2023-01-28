import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

def cal(list):
    result = 0
    for i in range(N-1):
        result += abs(list[i]-list[i+1])
    return result

max_ = 0

for p in permutations(nums):
    result = cal(p)
    if max_ < result:
        max_ = result

print(max_)