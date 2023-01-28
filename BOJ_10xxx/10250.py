T=int(input())
for t in range(T):
    H,W,N = map(int, input().split())
    print(f'{N%H}{N//H+1:02}') if N%H !=0 else print(f'{H}{N//H:02}')

'''
short coding

for t in [*open(0)][1:]:
    h, w, n = map(int, t.split())
    n-=1
    print((n%h + 1) * 100 + n//h + 1)
'''