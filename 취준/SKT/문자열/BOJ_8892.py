"""
팰린드롬
"""
import sys
from itertools import permutations

input = sys.stdin.readline

t = int(input())

answer = []

for i in range(t):
    k = int(input())
    ans = ''
    words = [input().strip() for _ in range(k)]

    for w1, w2 in permutations(words, 2):
        if w1 + w2 == (w1 + w2)[::-1]:
            ans = w1 + w2

    if ans == '':
        ans = 0
    answer.append(ans)

print(*answer)