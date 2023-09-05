"""
임스와 함께하는 미니게임

Y - 2명
F - 3명
O - 4명
"""
import sys

input = sys.stdin.readline


N, game = input().split()

people = [input().strip() for _ in range(int(N))]

chance = len(list(set(people)))
if game == 'Y':
    print(chance // 1)
if game == 'F':
    print(chance // 2)
if game == 'O':
    print(chance // 3)