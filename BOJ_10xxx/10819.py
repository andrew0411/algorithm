from itertools import permutations
N=int(input())
A=list(map(int, input().split()))
def eq(A:list):
    return sum([abs(A[i]-A[i+1]) for i in range(len(A)-1)])
max=0
for p in permutations(A, len(A)):
    res = eq(list(p))
    if max<res:
        max=res
print(max)