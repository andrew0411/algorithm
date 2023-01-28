l=sorted(list(map(int,input().split())))
if len(set(l)) == 1:
    print(10000+l[0]*1000)
elif len(set(l)) == 2:
    print(1000+l[1]*100)
else:
    print(l[2]*100)