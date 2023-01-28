import sys
input = sys.stdin.readline

N = int(input())
price = [0] * N
for i in range(N):
    price[i] = float(input())
print(f'{sorted(price)[1]:.2f}')

'''
short coding

n,*L=map(float,open(0))
print('%.2f'%sorted(L)[1])
'''
