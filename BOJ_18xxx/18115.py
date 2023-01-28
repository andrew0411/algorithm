import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

skills = deque(list(map(int, input().split())))

original = deque()
cards = 1

while skills:
    skill = skills.pop()

    if skill == 1:
        original.appendleft(cards)
        cards += 1

    elif skill == 2:
        temp = original.popleft()
        original.appendleft(cards)
        original.appendleft(temp)
        cards += 1

    elif skill == 3:
        original.append(cards)
        cards += 1
        
print(*original)