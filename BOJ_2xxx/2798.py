from itertools import combinations
N, M = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
max_n = 0
for i in combinations(nums, 3):
    temp = sum(i)
    if max_n < temp <= M:
        max_n = temp
print(max_n)