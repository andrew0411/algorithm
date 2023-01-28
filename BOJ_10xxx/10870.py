n=int(input())
a,b=0,1
for i in range(n-1):
    t=a+b
    a=b
    b=t
print(a) if n==0 else print(b)