N=int(input())
N_ls=list(map(int, input().split()))
M=int(input())
M_ls=list(map(int, input().split()))

def multiply(arr):
    return eval('*'.join([str(n) for n in arr]))
A = multiply(N_ls)
B = multiply(M_ls)

# Greatest Common Divisor
def GCD(x, y):
    while y != 0:
        t = x % y
        (x, y) = (y, t)
    return abs(x)

print(str(GCD(A, B))[-9:])