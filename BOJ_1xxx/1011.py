t=int(input())

def get(start, end):
    d = end - start
    n = 0
    while True:
        if d<= n*(n+1):
            break
        n+=1
    
    if d <= n ** 2:
        return 2 * n - 1
    if d > n ** 2:
        return 2 * n
result=[]
for i in range(t):
    a, b = map(int, input().split())
    result.append(get(a, b))
print(*result, sep='\n')