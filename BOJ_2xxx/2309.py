from itertools import combinations
k = [int(input()) for i in range(9)]
for _ in combinations(k, 7):
    if sum(_) == 100:
        print(*sorted(_), sep='\n')
        break