import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0

for (i, j, k) in combinations(range(N), 3):
    temp = cards[i] + cards[j] + cards[k]
    if result <= temp <= M:
        result = temp
print(result)