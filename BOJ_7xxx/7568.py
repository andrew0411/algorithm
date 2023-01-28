N=int(input())
ls=[]
idx=[]
for i in range(N):
    w,h=map(int,input().split())
    ls.append((w,h))
for i in ls:
    cnt=0
    for j in ls:
        if i[0]<j[0] and i[1]<j[1]:
            cnt+=1
    idx.append(cnt+1)
print(*idx)