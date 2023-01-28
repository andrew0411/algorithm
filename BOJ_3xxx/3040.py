from itertools import combinations

nums = []
for i in range(9):
    nums.append(int(input()))
for i in combinations(nums, 2):
    if sum(i) == sum(nums) - 100:
        nums.remove(i[0])
        nums.remove(i[1])
        print(*nums, sep='\n')