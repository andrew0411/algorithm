x=input().split('-')
num=0
for i in map(int,x[0].split('+')):
    num += i
for i in x[1:]:
    for j in map(int, i.split('+')):
        num -= j
print(num)