nums = []
while True:
    n = int(input())
    if n!= 0:
        nums.append(n)
    else:
        break

arr = [False, False] + [True] * (123456*2)
for i in range(2, 123456):
    if arr[i]:
        for j in range(i*2, len(arr), i):
            arr[j] = False
def get(n):
    return sum(arr[n+1:2*n+1])

for n in nums:
    print(get(n))