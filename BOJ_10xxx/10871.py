a, x = map(int, input().split())
l = list(map(int, input().split()))
for i in range(a):
    if l[i] < x:
        print(l[i], end=' ')