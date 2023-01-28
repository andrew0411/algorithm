nums = list(map(int, input().split()))
print(sum(map(lambda x:x**2, nums))%10)

'''
short coding

print(sum(int(a)**2for a in input()[::2])%10)
'''