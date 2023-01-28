t=int(input())
d_ls=[0]*t 
for i in range(t):
    d_ls[i]=int(input())
for d in d_ls:
    max=0
    for t in range(1, d+1):
        if (d-t-t**2)>=0:
            if max<t:
                max=t
    print(max)