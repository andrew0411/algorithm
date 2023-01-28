n = int(input())
# 50000 ** 0.5 = 223.61
nums = [0, 1]

for i in range(2, 50001):
    min_val = 100
    j = 1
    while j**2 <= i:
        min_val = min(min_val, nums[i - j**2])
        j += 1 
    nums.append(min_val+1)
print(nums[n])