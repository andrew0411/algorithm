X=int(input())
N=int(input())
a=[0]*N
b=[0]*N
for i in range(N):
    a[i], b[i] = map(int, input().split())
print('Yes' if X==sum([a[i]*b[i] for i in range(N)]) else 'No')