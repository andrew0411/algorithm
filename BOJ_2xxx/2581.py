M=int(input())
N=int(input())
def isPrime(n):
    if n==1:
        return 0
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return 0
        return 1
all = 0
cnt = 0
min = 0
for i in range(M, N+1):
    if isPrime(i):
        if cnt == 0:
            min = i
        all += i
        cnt += 1
print(all if cnt!=0 else -1)
print(min if cnt!=0 else '')
# 132ms, 395B

# if cnt == 0:
#     print(-1)
# else:
#     print(all)
#     print(min)
# 136ms, 397B