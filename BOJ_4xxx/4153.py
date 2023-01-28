result = []
while True:
    nums = sorted(list(map(int, input().split())))
    if sum(nums) == 0:
        print(*result, sep='\n')
        break
    
    if nums[-1]**2==nums[0]**2 + nums[1]**2:
        result.append('right')
    else:
        result.append('wrong')