n=list(map(int,input().split()))
ref=[1, 1, 2, 2, 2, 8]
res=[ref[i]-n[i] for i in range(6)]
print(*res)