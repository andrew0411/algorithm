def hansu(x:int)->int:
    if x//100==0:
        return True
    else:
        a=[int(i) for i in str(x)]
        if a[0]+a[2]==2*a[1]:
            return True
        else:
            return False
n=int(input())
count=0
for i in range(n):
    if hansu(i+1):
        count+=1
print(count)