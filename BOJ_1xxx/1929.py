m,n=map(int, input().split())

def get(num):
    if num==1:
        return 0
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return 0
        return 1
    
for i in range(m, n+1):
    if get(i):
        print(i)