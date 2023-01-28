N,M=map(int, input().split())
ks=list(map(int, input().split()))
sum_ls=[]
for i in range(1, N+1):
    for k in ks:
        if i%k == 0:
            sum_ls.append(i)
print(sum(set(sum_ls)))