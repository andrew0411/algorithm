n = int(input())
nums = map(int, input().split())
prime = 0
for num in nums:
    error = 0
    if num > 1 :
        for i in range(2, num): 
            if num % i == 0:
                error += 1
        if error == 0:
            prime += 1
print(prime)